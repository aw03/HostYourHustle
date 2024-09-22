import streamlit as st

st.set_page_config(
    page_title="Home",
)

st.write("# Welcome to Host Your Hustle!")

st.sidebar.success("Please Choose To Navigate to a page")

# Initialize session state to store data
if 'user_data' not in st.session_state:
    st.session_state['user_data'] = {}