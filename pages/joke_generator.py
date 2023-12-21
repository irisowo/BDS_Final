import streamlit as st
from openai import OpenAI
from functools import partial
from dotenv import load_dotenv

load_dotenv()

def get_joke(keyword, temperature=0.7):
    # Simulating an API call to OpenAI's GPT-3
    # return f'{keyword} Hahaha'
    client = OpenAI()
    prompt = f'Create a joke containing the word \"{keyword}\".'
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=temperature,
        max_tokens=150
    )
    return response.choices[0].text.strip()

st.title('Joke Generator')
st.write('Generate a joke based on a vocabulary you give.')

keyword = st.text_input('Enter a vocabulary')

# If the user has selected a topic, we generate a question
if st.button('Generate Joke'):
    # Here we would connect to GPT-3 to get a fill-in-the-blank style question
    # The prompt to GPT-3 should be crafted based on the selected topic

    # Simulate a response from GPT-3 (or another AI API)
    joke = get_joke(keyword)

    st.write(joke)


# if 'correct' not in st.session_state:
#     st.session_state.correct = False
# if 'page' not in st.session_state:
#     st.session_state.page = 'question'
# if st.session_state.page == 'question':
#     question_page()
# elif st.session_state.page == 'result':
#     result_page()
    
from PIL import Image
#Image In Sidebar 
with st.sidebar.container():
    image = Image.open(r"images/character.png")  
    st.image(image, use_column_width=True)
