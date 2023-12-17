import streamlit as st
import openai
from functools import partial

# with open('../api_key.txt', 'r') as f:
#     api_key = f.read()
# openai.api_key = api_key

def get_question(topic, temperature=0.7):
    # Simulating an API call to OpenAI's GPT-3
    return '___ is the capital of France.\nA. Paris \nB. London \nC. Berlin \nD. Rome'
    prompt = f'Create a fill-in-the-blank question about {topic} with multiple choice answers in the format: \n\n___ is the capital of France.\nA. Paris \nB. London \nC. Berlin \nD. Rome'
    response = openai.Completion.create(
        engine='davinci',
        prompt=prompt,
        temperature=temperature,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def check_answer(question, answer):
    # Simulating an API call to OpenAI's GPT-3
    st.session_state.correct = True
    st.write('Correct!' if st.session_state.correct else 'Incorrect!')
    return
    prompt = f'Question: {question}\nAnswer: {answer}\nYou should only respond True or False.'
    response = openai.Completion.create(
        engine='davinci',
        prompt=prompt,
        temperature=0.7,
        max_tokens=150
    )
    return response.choices[0].text.strip()


st.title('Fill in the Blank Exercises')
st.write('Complete the sentences by filling in the missing words.')

# Topic selection
topic = st.selectbox('Select the topic', ['Science', 'History', 'Art', 'Technology', 'Literature'])

# If the user has selected a topic, we generate a question
if st.button('Generate Question'):
    # Here we would connect to GPT-3 to get a fill-in-the-blank style question
    # The prompt to GPT-3 should be crafted based on the selected topic

    # Simulate a response from GPT-3 (or another AI API)
    question_with_options = get_question(topic)

    # TODO - Parse the response from GPT-3 to get the question and options
    tmp = question_with_options.split('\n')
    question = tmp[0]
    options = tmp[1:]
    st.write(question)
    for option in options:
        st.button(option[3:], on_click=partial(check_answer, question, option[3:]))

    
    # Display the question and options (for now, let's assume they are returned in a structured format)
    # st.write(question_with_options)
    # You could parse the 'question_with_options' to separate the question and options and then display them here