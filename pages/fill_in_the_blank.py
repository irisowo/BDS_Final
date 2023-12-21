import streamlit as st
import openai
from functools import partial

# with open('../api_key.txt', 'r') as f:
#     api_key = f.read()
# openai.api_key = api_key

def get_question(topic, temperature=0.7):
    # Simulating an API call to OpenAI's GPT-3
    return 'Question:\n___ is the capital of France.\nOption:\nA. Paris \nB. London \nC. Berlin \nD. Rome\nAnswer:\nA'
    prompt = f'Create a fill-in-the-blank question about {topic} with multiple choice answers in the format: \nQuestion:\n___ is the capital of France.\nOption:\nA. Paris \nB. London \nC. Berlin \nD. Rome\nAnswer:\nA'
    response = openai.Completion.create(
        engine='davinci',
        prompt=prompt,
        temperature=temperature,
        max_tokens=150
    )
    return response.choices[0].text.strip()

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
        tmp = question_with_options.split('\n')
        question = tmp[1]
        options = tmp[3:7]
        answer = tmp[8]
        st.session_state.answer = answer
        st.write(question)
        for option in options:
            st.button(option[3:], on_click=partial(check_answer, option[0]))

def result_page():
    st.title('Fill in the Blank Exercises')
    st.write('Complete the sentences by filling in the missing words.')
    if st.session_state.correct:
        st.write('Correct!')
    else:
        st.write('Incorrect!')
    
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