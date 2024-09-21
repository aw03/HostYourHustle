import streamlit as st
from neighborhoods import neighborhoods
from business import Business

st.title("Search For Businesses")
st.write("Please Use the Following Boxes to Filter Businesses")

neighborhood = st.multiselect("Filter By Neighborhood", neighborhoods)


st.write("Current Searches:")
st.write(st.session_state['user_data'])