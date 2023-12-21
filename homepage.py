import streamlit as st

st.title('Welcome to our English Learning Website')
st.write('Learn English in a fun and interactive way with our innovative online platform.')
st.write('Select a page from the sidebar to get started.')

from PIL import Image
#Image In Sidebar 
with st.sidebar.container():
    image = Image.open(r"images/character.png")  
    st.image(image, use_column_width=True)