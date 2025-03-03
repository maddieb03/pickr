import streamlit as st
from PIL import Image

st.set_page_config(page_title="Home", page_icon="🏠")

# changing background color
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #6ed6c3ff, #508692ff);
        border: 5px solid black;
        padding: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown("<h3 style='color: white; text-align: center;'>Welcome to</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='color: white; text-align: center;'>Pickr</h1>", unsafe_allow_html=True)

#add pic of logo
image = Image.open("og_logo.PNG")

st.markdown("<br>", unsafe_allow_html=True)

left_co, cent_co,last_co = st.columns(3)
with cent_co:
    st.image(image, use_container_width=True)