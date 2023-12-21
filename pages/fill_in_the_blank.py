import streamlit as st
import openai
from functools import partial
import json
from dotenv import load_dotenv

load_dotenv()

def get_question(topic, temperature=2):
    # Simulating an API call to OpenAI's GPT-3
    client = openai.OpenAI()

    system_msg = 'You are a helpful assistant designed to help students learn. Please help me create a fill-in-the-blank question with multiple choice answers in the format: \{"Question": "___ is the capital of France.", "Options": ["Paris", "London", "Taipei", "Beijing"], "Answer": "A" \}'
    prompt = f'Create a fill-in-the-blank question with multiple choice answers about {topic} in JSON format.'
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={ "type": "json_object" },
        messages=[
            {'role': 'system', 'content': system_msg},
            {'role': 'user', 'content': prompt}
        ],
        temperature=temperature,
        max_tokens=500
    )
    return json.loads(response.choices[0].message.content)

def check_answer(answer):
    answer = answer.strip()
    st.session_state.correct = (answer == st.session_state.answer)
    st.session_state.page = 'fill_result'
    return

def question_page():

    st.title('Fill in the Blank Exercises')
    st.write('Complete the sentences by filling in the missing words.')

    # Topic selection
    topic_list = ['Science', 'History', 'Art', 'Technology', 'Literature']
    topic = st.selectbox('Select the topic', topic_list, index=topic_list.index(st.session_state.topic))

    # If the user has selected a topic, we generate a question
    if st.button('Generate Question'):
        # Here we would connect to GPT-3 to get a fill-in-the-blank style question
        # The prompt to GPT-3 should be crafted based on the selected topic

        # Simulate a response from GPT-3 (or another AI API)
        st.session_state.topic = topic
        question_with_options = get_question(topic)

        # TODO - Parse the response from GPT-3 to get the question and options
        question = question_with_options['Question']
        options = question_with_options['Options']
        answer = question_with_options['Answer']
        st.session_state.answer = answer
        st.session_state.options = options
        st.write(question)
        idx2option = ['A', 'B', 'C', 'D']
        for idx, option in enumerate(options):
            st.button(option, on_click=partial(check_answer, idx2option[idx]))

def result_page():
    st.title('Fill in the Blank Exercises')
    st.write('Complete the sentences by filling in the missing words.')
    if st.session_state.correct:
        st.write('Correct!')
    else:
        st.write('Incorrect!')
        option2idx = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
        st.write(f'The correct answer is {st.session_state.options[option2idx[st.session_state.answer]]}')
    
    def back_to_question():
        st.session_state.page = 'fill_main'

    st.button('Next Question', on_click=back_to_question)

if 'correct' not in st.session_state:
    st.session_state.correct = False
if 'page' not in st.session_state:
    st.session_state.page = 'fill_main'
if 'topic' not in st.session_state:
    st.session_state.topic = 'Science'

this_page_states = ['fill_main', 'fill_result']
if st.session_state.page not in this_page_states:
    st.session_state.page = 'fill_main'

if st.session_state.page == 'fill_main':
    question_page()
elif st.session_state.page == 'fill_result':
    result_page()

from PIL import Image
#Image In Sidebar 
with st.sidebar.container():
    image = Image.open(r"images/character.png")  
    st.image(image, use_column_width=True)