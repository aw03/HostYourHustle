import streamlit as st
from neighborhoods import neighborhoods
from business import Business

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a page", ["Home", "Add Item", "About"])

# Home page
if page == "Home":
    st.title("Home Page")
    st.write("Welcome to the Home page!")
    st.write("You can search for things here!")

# Add Item page
elif page == "Add Item":
    st.title("Register Your Business")
    st.write("Please fill out the below boxes to register your profile")

    # Initialize session state to store data
    if 'user_data' not in st.session_state:
        st.session_state['user_data'] = []

    user_name = st.text_input('Enter your name or business name:')
    user_email = st.text_input('Enter your contact email:')
    user_neighborhood = st.selectbox('What neighborhood are you based in?', neighborhoods)
    user_services = st.multiselect('What is your service type', ["Beauty Services","Tailoring / Garments","Photography","Art / Crafts","Home Services", "Consulting Services", "Accounting"])
    user_socials = st.text_input('What are links to your socials: (separate by commas)')
    user_description = st.text_input('Description of your service')

    if st.button('Add Your Business'):
        if not (user_name == "" or user_email == "" or user_neighborhood == "" or user_services == []  or user_socials == "" or user_description == ""):
            new_item = Business(user_name,user_email,user_neighborhood,user_services,user_socials,user_description)
            st.session_state['user_data'].append(new_item)
            st.success(f'Item "{new_item}" added!')
        else:
            st.error('Please fill all fields before registering')

    st.write("Current items:")
    st.write(st.session_state['user_data'])

# About page
elif page == "About":
    st.title("About Page")
    st.write("This is the about page for the app.")
    st.write("Streamlit makes it easy to build interactive web apps using Python.")

