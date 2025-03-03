import streamlit as st

st.set_page_config(page_title="About", page_icon="ℹ️")

# changing background color to same as HOME page
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #6ed6c3ff, #32627dff);
        border: 5px solid black;
        padding: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("ℹ️ What is Pickr?")


st.markdown(
    """
    **Pickr** is a free and safe music and movie recommendation software. 
    With Pickr, you can:\n
    - Generate a list of songs/movies based off your inputed song(s)/movie(s)\n
    - Generate a list of songs/movies based off a given genre(s)\n
    - Retrieve Pickr data from previous visits when you log in\n

    ### The Developers
    **Pickr** was developed by *Madelyn Bullock*, *Rayan Chiadmi*, *Kaitlyn Green*, 
    *Mady Mitchell*, *Mallike Pamula*, and *Brianna Wang*
    """
)

#adding space before "Contact Us"
st.markdown("<br><br><br><br><br><br><br><br>", unsafe_allow_html=True)

st.markdown(
    """
    ### Contact Us
    Reach us by email with: **pickrSupport@gmail.com**
    """
)