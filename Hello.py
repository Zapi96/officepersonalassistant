# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
import openai
from redlines import Redlines
import clipboard
from chatgpt import get_completion_from_messages
from emails_correction import emails_correction




LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Personal Assistant",
        page_icon="🤖",
    )

    
    

    openai_api_key = st.sidebar.text_input('OpenAI API Key')

    st.title('Personal Assistant')

    st.header('Emails correction')

    expander = st.expander('Tool to improve emails')

    with expander:
      if "response" not in st.session_state: 
        st.session_state.response = ''

      if "messages" not in st.session_state: 
        st.session_state.messages = ''
      emails_correction(openai_api_key)

    

     


if __name__ == "__main__":
    run()
