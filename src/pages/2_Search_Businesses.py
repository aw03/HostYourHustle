import streamlit as st
from dropdowns import neighborhoods
from dropdowns import services
from business import Business

st.title("Search For Businesses")
st.write("Please Use the Following Dropdowns to Filter Businesses")

# Initialize session state to store data
if 'user_data' not in st.session_state:
    st.session_state['user_data'] = {}

st.header("Filters:")
neighborhood_filt = set(st.multiselect("Filter By Neighborhood", neighborhoods))
services_filt = set(st.multiselect("Filter By Services", services))

def is_filter_out(elt):
    if len(services_filt) != 0:
        if len(services_filt.intersection(elt.get_services)) == 0:
            return False
    if len(neighborhood_filt) != 0:
        if elt.get_neighborhood not in neighborhood_filt:
            return False
    return True


st.header("Current Searches:")

for elt in st.session_state['user_data'].values():
    if not is_filter_out(elt):
        continue
    st.markdown(
    """
    <hr style="border: 1px solid black; margin: 20px 0;">
    """,
    unsafe_allow_html=True
)
    st.header(elt.get_name)
    st.subheader("Services: " + ", ".join(elt.get_services))
    st.subheader("Based in: " + elt.get_neighborhood)
    st.write(elt.get_description)
    st.write("Email: " + elt.get_contact)
    st.write("\n".join(elt.get_socials))
