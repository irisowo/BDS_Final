import util
import openai
import streamlit as st
from functools import partial
from dotenv import load_dotenv


def check_sentence(sentence, temperature=0.7):
    system_msg = 'You are a helpful assistant designed to help students learn. Please help me check the grammar of the following sentence.'
    client = openai.OpenAI()
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
    sentence = st.text_input('Enter a sentence')
    st.button('Check Grammar', on_click=partial(check_sentence, sentence))
        

def result_page():
    st.write(st.session_state.result)
    def back_to_sentence():
        st.session_state.page = 'sentence'
    st.button('Next Sentence', on_click=back_to_sentence)


def main():
    # get API
    load_dotenv()

    # Page Configuration 
    st.set_page_config(page_title= "Grammar checker", page_icon= "🐑")
    st.title("🐑 Grammar checker")
    util.render_sider()
    util.render_banner(r"lottie_files/analyze_robot.json")
    st.subheader('Check your grammar with the help of AI.')

    if 'page' not in st.session_state:
        st.session_state.page = 'grammar_main'

    this_page_states = ['grammar_main', 'grammar_result']
    if st.session_state.page not in this_page_states:
        st.session_state.page = 'grammar_main'

    if st.session_state.page == 'grammar_main':
        sentence_page()
    elif st.session_state.page == 'grammar_result':
        result_page()

main()