import pandas as pd
import streamlit as st
import time

st.write('''Streamlit simplifies the process of creating interactive web apps.
         However, it runs everything from top to bottom every time you make a change, so it will reload your data again and again.
         Also, it will loss the user input every time the app is reloaded.
         This can be a problem when you want to maintain the state of your app.
         This is why it is important to understand how to manage the state of your app.''')

st.write('---')

st.write('Here is an example, assume you have a variable x, you want to change it with a slider.')
x = 5
st.markdown(f'The initial value of x is :red[{x}].')
st.write('Note that the value changed below will not impact x here. And it can not be used for other pages.')
x = st.slider('Change the value of x', 0, 10, x)
st.write(f'The value of x now is :red[{x}], changed by slider.')

st.write('---')
st.write('Now, I put y in a session state, so that it can be used in other pages and will not be lost when the app is reloaded.')

if 'y' not in st.session_state:
    st.session_state.y = 5
else:
    print(st.session_state.y)
    print('y is already in session state.')
    
st.write(f"The initial value of y in 'st.session_stat' is :green[{st.session_state.y}].")
st.slider('Change the value of y', 0, 10, key='y')
st.write(f"The value of y now is :green[{st.session_state.y}], changed by slider.")


st.write('---')
st.write('Here is an example of caching data.')
st.write('The data is loaded from a csv file. It will take a while to load the data.')
def load_data(url):
    df = pd.read_csv(url)  # 👈 Download the data
    time.sleep(3)  # 👈 Simulate a slow data source
    return df

with st.spinner("Loading data..."):
    df = load_data("data\GEM_Coalpowerplant.csv")
st.dataframe(df)
st.write('Without caching, the data will be reloaded every time the app is reloaded. It will take a while to load the data again.')
st.button("Rerun")


@st.cache_data  # 👈 Add the caching decorator
def load_data2(url):
    df = pd.read_csv(url)
    time.sleep(3)  # 👈 Simulate a slow data source
    return df
st.write('With caching, the data will be loaded only once. It will not be reloaded every time the app is reloaded.')
with st.spinner("Loading data..."):
    df2 = load_data2("data\GEM_Coalpowerplant.csv")
st.dataframe(df2)

st.button("Rerun cache_data")