import streamlit as st

# Title of the app
st.title("Scrollable Text Information")

# Create an expander
with st.expander("Click to see more information", expanded=False):
    st.write("""
    This is some detailed text information that can be scrolled down. 
    You can include any content here, such as:
    
    - **Point 1**: Explanation for point 1.
    - **Point 2**: Explanation for point 2.
    - **Point 3**: Explanation for point 3.
    
    You can also add more text or even images, links, etc.
    
    ### Additional Information
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
    Quisque at semper lorem, vitae congue libero. 
    Integer sit amet lacus neque. Cras condimentum sapien vel orci venenatis, 
    vitae varius quam facilisis.
    
    You can include as much text as needed, and it will be scrollable within this section.
    """)

# Optional: Add more content outside the expander
st.write("This is additional content outside the expander.")
