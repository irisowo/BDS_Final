import  util
import streamlit as st
from openai import OpenAI
from functools import partial
from dotenv import load_dotenv


def get_joke(keyword, temperature=0.7):
    # Simulating an API call to OpenAI's GPT-3
    # return f'{keyword} Hahaha'
    client = OpenAI()
    system_msg = 'You are a humorous assistant. Please tell some jokes. You should only respond at a maximum of 4 sentences.'
    prompt = f'Tell me a joke with the word {keyword} in it.'
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {'role': 'system', 'content': system_msg},
            {'role': 'user', 'content': prompt}
        ],
        temperature=temperature,
        max_tokens=50,
        frequency_penalty=2,
    )
    return response.choices[0].message.content.strip() 


def main():
    # get API 
    load_dotenv()

    # Page Configuration 
    st.set_page_config(page_title= "Joke Generator", page_icon= "🐼")
    st.title('🐼 Joke Generator')
    util.render_sider()
    util.render_banner(r"lottie_files/power_robot.json")

    st.subheader('Generate a joke based on a vocabulary you give.')
    keyword = st.text_input('Enter a vocabulary')

    # If the user has selected a topic, we generate a question
    if st.button('Generate Joke'):
        # Here we would connect to GPT-3 to get a fill-in-the-blank style question
        # The prompt to GPT-3 should be crafted based on the selected topic
        # Simulate a response from GPT-3 (or another AI API)
        joke = get_joke(keyword)
        st.write(joke)


main()