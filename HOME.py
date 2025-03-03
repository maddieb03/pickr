import streamlit as st
from PIL import Image

st.set_page_config(page_title="Home", page_icon="🏠")

# changing background color: gradient of Pickr colors
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



#welcome message
st.markdown("<h3 style='color: white; text-align: center;'>Welcome to</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: white; text-align: center; font-size: 80px; font-weight: bold;'\
            >Pickr</p>", unsafe_allow_html=True)


#add pic of logo
image = Image.open("og_logo.PNG")


#displaying/centering logo
left_co, cent_co,last_co = st.columns(3) 
with cent_co:
    st.image(image, use_container_width=True)

# slogan(?)
st.markdown('<p style="color: #32627dff; text-align: center; font-size: 22px; font-weight: bold;">Music & \
            Movies Tailored to Your Taste</p>', unsafe_allow_html=True)


#adding space before more info
st.markdown("<br><br><br><br>", unsafe_allow_html=True)

#telling user about navigation -> sidebar
st.title("🗺️ Navigation")
st.markdown(
    """
    To navigate through the Pickr site, use the sidebar on the left side of your screen.
    You may have to open it using the arrow in the top-left corner.
    """
)