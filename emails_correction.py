import streamlit as st
from redlines import Redlines
from chatgpt import get_completion_from_messages

def emails_correction(openai_api_key):
    c1,c2,c3,c4 = st.columns(4)
    with c1:
        formality = st.selectbox('Formality:',['Informal','Formal'])
    with c2:
        simplicity = st.selectbox('Simplicity:',['Simple','Complex'])
    with c3:
        language = st.selectbox('Language:',['Spanish','English'])
        if language == 'Spanish':
            country = 'Spain'
        elif language == 'English':
            country = 'England'
    with c4:
        person = st.selectbox('Person:',['Client','Boss','Colleague'])   
    email = st.text_area('Introduce the email to be improved',height =300)
    prompt = f"""
    Improve the email delimited by triple backticks. /
    It must be {formality}, {simplicity} and written in {language} of {country}./
    Take into consideration that it is an email for a {person}.
    ```{email}```
    """
    promt2 = f"""
    Try again and improve your previous response. /
    Remember that it must be {formality}, {simplicity} and written in {language} of {country}./
    Take into consideration that it is an email for a {person}.
    """
    c1,c2,_,_,c5 = st.columns(5) 
    with c1:
        submitted = st.button('Submit',type='primary') 
    with c5:
        clear_response = st.button('Clear response') 

    if submitted and openai_api_key.startswith('sk-'):
        messages = [{'role':'system', 'content':'You are an assistant for a Data Engineer at Bluetab, an IBM Company.'},
                    {"role": "user", "content": prompt}]
        response = get_completion_from_messages(messages,openai_api_key)
        messages.append({"role": "assistant", "content": response})
        st.session_state.response = response
        st.session_state.messages = messages

    try_again = False
    if len(st.session_state.response)>0:
        with c2:
            try_again = st.button('Try again')

    if try_again ==True and openai_api_key.startswith('sk-'):
        st.session_state.messages.append({"role": "user", "content": promt2})
        response = get_completion_from_messages(st.session_state.messages,openai_api_key)
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.session_state.response = response

    if clear_response:
        st.session_state.response = ''
        st.session_state.messages = ''

    if len(st.session_state.response)>0:
        show_differences = st.checkbox('Show differences')
        if show_differences:
            diff = Redlines(email, st.session_state.response)
            diff_output = diff.output_markdown
            st.markdown(diff_output, unsafe_allow_html=True)
        else:
            st.write(st.session_state.response)