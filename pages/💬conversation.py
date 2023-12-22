import json
import util
import openai 
import pandas as pd 
import streamlit as st
from dotenv import load_dotenv


def main():
    # Read API key
    load_dotenv()

    # Page Configuration 
    st.set_page_config(page_title= "Conversation", page_icon= "💬")
    st.title("💬 Chatbot")
    util.render_sider()
    util.render_banner(r"lottie_files/talk_robot.json")

    # content
    st.subheader("Let's chat together")
    st.write("Users can use this page to ask ChatGPT general questions.")
    st.write("This can be a viable space to use when the ChatGPT is unavailable but someone has a OpenAI key to use.")

    # Initialize
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-3.5-turbo-0613"
    # Start the Chat History 
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun 
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
        
    # React to user input
    prompt = st.chat_input("Say something ... (ㆆᴗㆆ)")
    if prompt:
        # Display user message in chat message container 
        with st.chat_message("user"):
            st.markdown(prompt)
        # Add user message to chat history 
        st.session_state.messages.append({"role": "user", "content": prompt}) 
        
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            client = openai.OpenAI()

            stream = client.chat.completions.create(
                model = st.session_state["openai_model"],
                messages = [
                    {"role": m["role"], "content" : m["content"]}
                    for m in st.session_state.messages
                ],
                stream = True,
            )
            for chunk in stream:
                content = chunk.choices[0].delta.content
                if content is not None:
                    full_response += content
                    message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content" : full_response})

main()