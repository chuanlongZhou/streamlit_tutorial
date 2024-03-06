import streamlit as st
import pandas as pd

st.markdown('# Display text or data')


st.write('Directly display with st.write()')
st.write([1, 2, 3, 4, 5])
df = pd.read_csv('data\GEM_Coalpowerplant.csv')
st.write(df.head(10))
st.write('Streamlit has a fancy way to display data')

st.markdown('---')


st.markdown('# Markdown Examples')
st.markdown("### This is a h3 header")
# display a emoji symbol, smiley face
st.markdown('Streamlit can display emoji 😃')
st.markdown("*Streamlit* is **really** ***cool***. ")
st.markdown("[Streamlit](https://streamlit.io/) is a great tool for data science.")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors].''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)