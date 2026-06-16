

# Basic streamlit app(app_basic.)
# 1. Display a title: 'Welcome to Streamlit'
# 2.Shows a text input box for entering your name
# 3. When user click a button "Greet Me", display:
    # 'Hello,!'
    # Use:
    # st.title()
    # st.text_input()
    # st.button()
    # st.write()
    
    
import streamlit as st

# Display title
st.title("Welcome to Streamlit")

# Text input for user name
name = st.text_input("Enter your name")

# Button
if st.button("Greet Me"):
    st.write(f"Hello, {name}!")