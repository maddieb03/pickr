import streamlit as st

st.set_page_config(page_title="Home", page_icon="🏠")

st.sidebar.title("Navigation")  # Sidebar title
page = st.sidebar.radio("Go to", ["Home", "About", "Login", "Music", "Movies"])

st.title("Welcome")  # Home Page Title
st.write("This is the main page of the app.")