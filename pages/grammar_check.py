import streamlit as st
import openai
from functools import partial
from dotenv import load_dotenv

load_dotenv()

def check_sentence(sentence, temperature=0.7):
    # Simulating an API call to OpenAI's GPT-3
    client = openai.OpenAI()

    system_msg = 'You are a helpful assistant designed to help students learn. Please help me check the grammar of the following sentence.'
    
    response = client.chat.completions.create(
        model='gpt-3.5-turbo-1106',
        messages=[
            {'role': 'system', 'content': system_msg},
            {'role': 'user', 'content': sentence}
        ],
        temperature=temperature,
        max_tokens=150
    )
    result = response.choices[0].message.content.strip()
    st.session_state.result = result
    st.session_state.page = 'grammar_result'


def sentence_page():

    st.title('Grammar Check')
    st.write('Check your grammar with the help of AI.')

    sentence = st.text_input('Enter a sentence')

    st.button('Check Grammar', on_click=partial(check_sentence, sentence))
        


def result_page():
    st.title('Grammar Check')
    st.write('Check your grammar with the help of AI.')

    st.write(st.session_state.result)

    def back_to_sentence():
        st.session_state.page = 'sentence'

    st.button('Next Sentence', on_click=back_to_sentence)

if 'page' not in st.session_state:
    st.session_state.page = 'grammar_main'

this_page_states = ['grammar_main', 'grammar_result']
if st.session_state.page not in this_page_states:
    st.session_state.page = 'grammar_main'

if st.session_state.page == 'grammar_main':
    sentence_page()
elif st.session_state.page == 'grammar_result':
    result_page()

from PIL import Image
#Image In Sidebar 
with st.sidebar.container():
    image = Image.open(r"images/character.png")  
    st.image(image, use_column_width=True)