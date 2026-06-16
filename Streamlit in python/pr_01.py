# print('world hello');

import streamlit as st
import pandas as pd
st.write("Hello world")


st.title('Hello streamlit')
st.write('this is my first streamlit app')
st.header("Welcome to streamlit")
st.subheader('This is subheader')
st.text("this is plain text")

# buttons and checkbox and slider
if st.button('click me!'):
    st.write('Button Clicked...')

agree = st.checkbox('I agree')
if agree:
    st.write('you agreed')
    
level = st.slider("select a level :", 1 ,10 ,5)
st.write(f"Selected level : {level}")




# file uploader function
uploaded_file = st.file_uploader('Upload a file' ,type=['csv' , 'txt'])
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df.head())