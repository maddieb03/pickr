import streamlit as st

st.set_page_config(page_title="Log in", page_icon="👤")


st.markdown('<div class="gray-box">', unsafe_allow_html=True)  # Start the gray box

st.subheader("👤 Log in")  # Title inside the box
st.caption("Logging in retrieves your data and preferences from your previous visits for a more personalized experience.")


# Login Form
with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.form_submit_button("Login")

st.markdown("</div>", unsafe_allow_html=True)  # Close the gray box

# Authentication Logic
if login_button:
    if username == "admin" and password == "1234": #EXAMPLE!
        st.success("Login Successful!")
        st.session_state["authenticated"] = True
    else:
        st.error("Invalid credentials")
