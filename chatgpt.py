import openai
import os

def get_completion(prompt,api_key, model="gpt-3.5-turbo"):
    
    client = openai.OpenAI(api_key=api_key)

    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message["content"]

def get_completion_from_messages(messages,api_key, model="gpt-3.5-turbo", temperature=0):
    
    client = openai.OpenAI(api_key=api_key)
    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message.content