import streamlit as st

# Initialize session state to store data
if 'user_data' not in st.session_state:
    st.session_state['user_data'] = []

# Title of the app
st.title('Streamlit App with Sidebar')

# Sidebar title
st.sidebar.title("Options")

# Sidebar input text box
new_item = st.sidebar.text_input('Add a new item')

# Sidebar Add button
if st.sidebar.button('Add Item'):
    if new_item:
        # Add the new item to the list
        st.session_state['user_data'].append(new_item)
        st.sidebar.success(f'Item "{new_item}" added successfully!')
    else:
        st.sidebar.error('Please enter an item before adding.')

# Display current items in the main area
st.write('Current items:')
st.write(st.session_state['user_data'])

# Sidebar button to process data
if st.sidebar.button('Process Data'):
    st.write('Processing your data...')
    # Example of simple data processing (just showing the length of the list)
    st.write(f'Total items: {len(st.session_state["user_data"])}')

# Additional main area content (optional)
st.write('You can use the sidebar to add and process items.')
