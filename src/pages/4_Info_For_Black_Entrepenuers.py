import streamlit as st

# Title of the app
st.title("Find Information To Grow Your Hustle!")

# Create an expander
with st.expander("Beauty and Hair", expanded=False):
    st.header("Get a Hair care liscence to start towards opening a shop!")
    st.write(
        """
    A hair stylist license is your credentials or certification that demonstrate you have graduated from an approved hairdressing school or program. Hair stylists need to pass board exams, administered at the state level, to obtain their hairdresser license and practice in that state.
    Find information here! \n   https://www.beautyschoolsdirectory.com/programs/hair-design/licensing"""
    )

with st.expander("Home Repair", expanded=False):
    st.header("Become a Certified Renovator!")
    st.write(
        """
    This certification is awarded to renovators who complete an EPA-accredited training course. The course includes 8 hours of training, including 2 hours of hands-on learning. To maintain certification, renovators must take a refresher course before their current certification expires.
Certifications include: Certified Remodeler (CR), Certified Remodeler Specialist (CRS), Certified Remodeler Associate (CRA), and other certifications.
             \n https://www.mass.gov/how-to/apply-for-an-individual-electrical-or-systems-license
    """
    )

with st.expander("Gardening", expanded=False):
    st.header("Improve your Gardening Credibility")
    st.write(
        """
    National Association of Landscape Professionals (NALP) certifications
These certifications include landscape industry certified manager, landscape industry certified technician, and landscape industry certified lawn care manager. To earn these certifications, applicants may need to pass a multiple-choice exam or a hands-on field test.
ISA Certified Arborist
This certification is voluntary and helps consumers identify qualified tree care professionals. \n
https://www.landscapeprofessionals.org/LP/LP/Certification/Certification-NALP.aspx"""
    )

# Optional: Add more content outside the expander
st.write("More info to come!")
