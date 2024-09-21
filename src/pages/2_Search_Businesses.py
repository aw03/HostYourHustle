import streamlit as st
from neighborhoods import neighborhoods
from business import Business

st.title("Search For Businesses")
st.write("Please Use the Following Boxes to Filter Businesses")

neighborhood = st.multiselect("Filter By Neighborhood", neighborhoods)

st.write("Current Searches:")
for elt in st.session_state['user_data'].values():
    st.markdown(
    """
    <hr style="border: 2px solid black; margin: 20px 0;">
    """,
    unsafe_allow_html=True
)
    st.header(elt.get_name)
    st.subheader(", ".join(elt.get_services))
    st.subheader("Based in: " + elt.get_neighborhood)
    st.write(elt.get_description)
    st.write("\n".join(elt.get_socials))

# st.write(st.session_state['user_data'])

# st.dataframe(st.session_state['user_data'])

# tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
# tab1.write("this is tab 1")
# tab2.write("this is tab 2")
