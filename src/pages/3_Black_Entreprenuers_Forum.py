import streamlit as st
from datetime import datetime

# Title of the forum
st.title("Hustlers Forum")

# Create a session state to store comments
if 'comments' not in st.session_state:
    st.session_state.comments = []

# Section to write a new comment
st.header("Share with the Community!")

# Input fields for the post
name = st.text_input("Your Name")
contact = st.text_input("Your Contact (optional)")
comment = st.text_area("Your Post")

# Button to submit the comment
if st.button("Submit"):
    if name and comment:
        # Capture the current time for the comment
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Store the new comment
        st.session_state.comments.append({
            'name': name,
            'contact': contact,
            'comment': comment,
            'timestamp': timestamp
        })
        st.success("Your post has been submitted!")
    else:
        st.error("Please fill in both your name and comment.")

# Section to display all comments
st.header("All Comments")

# Display all the comments with timestamps
if st.session_state.comments:
    for comment_data in st.session_state.comments[::-1]:  # Reverse order to show the latest first
        st.markdown("---")
        st.markdown(f"**{comment_data['name']}** at {comment_data['timestamp']}")
        if comment_data['contact']:
            st.markdown(f"Contact: {comment_data['contact']}")
        st.markdown(f"> {comment_data['comment']}")
        
else:
    st.write("No comments yet.")
