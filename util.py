import json
from PIL import Image
import streamlit as st 
from streamlit_lottie import st_lottie


def import_json(path):
    with open(path, "r", encoding="utf8", errors="ignore") as file:
        url = json.load(file)
        return url


def render_sider():
    with st.sidebar.container():
        image = Image.open(r"images/character.png")  
        st.image(image, use_column_width=True)


def render_banner(file_path, height=400):
    data_oracle = import_json(file_path)
    st_lottie(data_oracle, height=height, key="oracle")