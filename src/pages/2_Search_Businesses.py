import streamlit as st
from dropdowns import neighborhoods
from business import Business

st.title("Search For Businesses")
st.write("Please Use the Following Boxes to Filter Businesses")

# Initialize session state to store data
if 'user_data' not in st.session_state:
    st.session_state['user_data'] = {}

neighborhood = st.multiselect("Filter By Neighborhood", neighborhoods)

st.header("Current Searches:")
for elt in st.session_state['user_data'].values():
    st.markdown(
    """
    <hr style="border: 1px solid black; margin: 20px 0;">
    """,
    unsafe_allow_html=True
)
    st.header(elt.get_name)
    st.subheader(", ".join(elt.get_services))
    st.subheader("Based in: " + elt.get_neighborhood)
    st.write(elt.get_description)
    st.write("Email: " + elt.get_contact)
    st.write("\n".join(elt.get_socials))