import streamlit as st

st.set_page_config(
    page_title="Home",
)

st.write("# Welcome to Host Your Hustle!")
st.write("## Economic mobility in the Black Community")

st.markdown(
    """
    <hr style="border: 1px solid black; margin: 20px 0;">
    """,
    unsafe_allow_html=True
)

welcome_message = """
Welcome to Host Your Hustle, the ultimate platform designed to bridge the economic gap in the Black community. Our mission is to empower local hustlers and gig workers by connecting them with affordable services and essential resources to thrive in their entrepreneurial journeys.

**For Customers:** 

Discover a diverse range of affordable services offered by talented Black entrepreneurs in Boston. Whether you need a handyman, a graphic designer, or a personal trainer, Host Your Hustle makes it easy to book gigs from trusted professionals within your community.

**For Entrepreneurs:**

Host Your Hustle is your go-to resource for starting and growing your business. Access vital information on certification requirements, find spaces for running your business, and learn everything you need to kickstart your hustle. Our platform provides comprehensive guides, expert advice, and a supportive community to help you succeed.


***Join Host Your Hustle today and be a part of a movement that champions economic equity and entrepreneurial spirit in the Black community. Let's hustle together!***
"""


st.write(welcome_message)

st.write()

st.sidebar.success("Please Choose To Navigate to a page")

# Initialize session state to store data
if 'user_data' not in st.session_state:
    st.session_state['user_data'] = {}