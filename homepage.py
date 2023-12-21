import util
import openai 
import pandas as pd 
import streamlit as st 
from streamlit_lottie import st_lottie
from streamlit_folium import folium_static


if __name__ == '__main__':
    # Page Configuration 
    st.set_page_config(
        page_title= "Language assistant",
        page_icon= "🤖"
    )

    st.title("Language Assistant 🤖")

    # Banner
    util.render_banner(r"lottie_files/hi_robot.json")

    st.subheader("Introduction")
    st.write("""Hello! Welcome to the world of language learning with me, \
                your dedicated language companion. :blossom:""")
    st.write("""
                Whether you're embarking on a linguistic adventure for the first time or seeking to enhance your existing skills, \
                I'm here to guide you through the exciting journey of mastering new languages.""")
    st.write("""
                Together, we'll explore the intricacies of grammar, expand your vocabulary, and practice conversational skills. \
                Remember, every step you take in this language-learning journey brings you closer to fluency.""")
    st.write("""
                So, let's embark on this rewarding endeavor together, and don't hesitate to ask any questions along the way!""")



    util.render_sider()
