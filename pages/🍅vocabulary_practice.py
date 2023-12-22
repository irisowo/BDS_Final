import json
import util
import openai
import streamlit as st
from functools import partial
from dotenv import load_dotenv


def get_question(topic, temperature=1):
    # Simulating an API call to OpenAI's GPT-3
    client = openai.OpenAI()

    system_msg = 'You are a helpful assistant designed to help students learn. Please help me create a translation question with traditional chinese and english vocabulary in the format: \{"Chinese": "葡萄", "English": "grapes" \}'
    prompt = f'Create a translation question about the topic "{topic}" and avoid "{topic}" itself in JSON format.'
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={ "type": "json_object" },
        messages=[
            {'role': 'system', 'content': system_msg},
            {'role': 'user', 'content': prompt}
        ],
        temperature=temperature,
        max_tokens=150
    )
    print(response.choices[0].message.content)
    return json.loads(response.choices[0].message.content)


def check_answer(answer):
    answer = answer.strip()
    st.session_state.correct = (answer == st.session_state.english)
    if not st.session_state.correct:
        double_check_answer(answer)
    st.session_state.has_generated = False
    st.session_state.page = 'vocabulary_result'


def double_check_answer(answer):
    # Simulating an API call to OpenAI's GPT-3
    client = openai.OpenAI()

    system_msg = 'You are a helpful assistant designed to help students learn. Please help me determine if the answer is correct or not. You should respond with either True or False.'
    prompt = f'The english translation of {st.session_state.chinese} is {answer}.'
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {'role': 'system', 'content': system_msg},
            {'role': 'user', 'content': prompt}
        ],
        max_tokens=150
    )
    st.session_state.correct = response.choices[0].message.content.strip() == 'True'


def question_page():
    if not st.session_state.has_generated:
        # Topic selection
        topic_list = ['Science', 'History', 'Art', 'Technology', 'Literature']
        topic = st.selectbox('Select the topic', topic_list, index=topic_list.index(st.session_state.topic))
        st.button('Generate Vocabulary', on_click=partial(write_question, topic))
    else:
        st.write(st.session_state.chinese)
        user_input = st.text_input('Enter the English translation')
        st.button('Check Answer', on_click=partial(check_answer, user_input))


def write_question(topic):
    st.session_state.topic = topic
    ch_and_en_vocabulary = get_question(topic)
    print(ch_and_en_vocabulary)

    ch = ch_and_en_vocabulary['Chinese']
    en = ch_and_en_vocabulary['English']
    st.session_state.chinese = ch
    st.session_state.english = en
    st.session_state.has_generated = True


def result_page():
    if st.session_state.correct:
        st.success('Correct!')
    else:
        st.warning('Incorrect!')
        st.write(f"""**The correct answer should be {st.session_state.english}**""")
    
    def back_to_question():
        st.session_state.page = 'vocabulary_main'

    st.button('Next Question', on_click=back_to_question)


def main():
    # get API
    load_dotenv()

    # Page Configuration 
    st.set_page_config(page_title= "Vocabulary Practice", page_icon= "🐼")
    st.title("🍅 Vocabulary Practice")
    util.render_sider()
    util.render_banner(r"lottie_files/oracle_robot.json")
    st.subheader('Translate the following words from Chinese to English.')

    if 'correct' not in st.session_state:
        st.session_state.correct = False
    if 'has_generated' not in st.session_state:
        st.session_state.has_generated = False
    if 'page' not in st.session_state:
        st.session_state.page = 'vocabulary_main'
    if 'topic' not in st.session_state:
        st.session_state.topic = 'Science'

    this_page_states = ['vocabulary_main', 'vocabulary_result', 'disabled']
    if st.session_state.page not in this_page_states:
        st.session_state.page = 'vocabulary_main'

    if st.session_state.page == 'vocabulary_main':
        question_page()
    elif st.session_state.page == 'vocabulary_result':
        result_page()


main()