import streamlit as st

st.markdown('---')
col1, col2, col3 = st.columns(3)
with col1:
    st.write('This is a button')
    st.button("Reset", type="primary")
    if st.button('Say hello'):
        st.write('Why hello there')
    else:
        st.write('Goodbye')
    
with col2:
    st.write('This is a selectbox')
    agree = st.checkbox('I agree')
    if agree:
        st.write('Great!')
    
with col3:
    st.write('This is a toggle button')
    on = st.toggle('Activate feature')

    if on:
        st.write('Feature activated!')

st.markdown('---')
col1, col2, col3 = st.columns(3)
with col1:
    st.write('This is a radio button')
    ans = st.radio(
        "Please select:",
        ["a", "b", "c"],
        captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."])
    st.write(f'You selected {ans}.')
    
with col2:
    st.write('This is a selectbox')
    option = st.selectbox(
        'How would you like to be contacted?',
        ('Email', 'Home phone', 'Mobile phone'))

    st.write('You selected:', option)
    
with col3:
    st.write('This is a multiselect')
    options = st.multiselect(
        'What are your favorite colors',
        ['Green', 'Yellow', 'Red', 'Blue'],
        ['Yellow', 'Red'])

    st.write('You selected:', options)
    
st.markdown('---')
col1, col2, col3 = st.columns(3)
with col1:
    st.write('This is a slider')
    values = st.slider(
        'Select a range of values',
        0.0, 100.0, (25.0, 75.0))
    st.write('Values:', values)
    
with col2:
    st.write('This is a text input')
    title = st.text_input('Movie title', 'Life of Brian')
    st.write('The current movie title is', title)

import datetime
with col3:
    st.write('This is a number input')
    number = st.number_input('Insert a number')
    st.write('The current number is ', number)
    
st.markdown('---')
col1, col2, col3 = st.columns(3)
with col1:
    st.write('This is a file uploader')
    uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        st.write(bytes_data)
with col2:
    st.write('This is a color picker')
    color = st.color_picker('Pick A Color', '#00f900')
    st.write('The current color is', color)
with col3:
    st.write('This is a date input')
    d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
    st.write('Your birthday is:', d)
    
st.markdown('---')
st.write('And more...')
