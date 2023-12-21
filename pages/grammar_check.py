import streamlit as st
import openai
from functools import partial

# with open('../api_key.txt', 'r') as f:
#     api_key = f.read()
# openai.api_key = api_key

def check_sentence(topic, temperature=0.7):
    # Simulating an API call to OpenAI's GPT-3
    result = 'Good'
    st.session_state.result = result
    st.session_state.page = 'grammar_result'
    return
    prompt = f'Create a fill-in-the-blank question about {topic} with multiple choice answers in the format: \nQuestion:\n___ is the capital of France.\nOption:\nA. Paris \nB. London \nC. Berlin \nD. Rome\nAnswer:\nA'
    response = openai.Completion.create(
        engine='davinci',
        prompt=prompt,
        temperature=temperature,
        max_tokens=150
    )
    return response.choices[0].text.strip()


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