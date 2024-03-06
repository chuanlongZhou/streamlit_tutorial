import streamlit as st
import numpy as np

st.markdown('### Image')
st.write('If you want to improve the speed of your app, you can use the `st.image` method to display pre-generated images.')
st.image('data\image.jpg', caption='Cute dogs')
st.image('https://images.unsplash.com/photo-1548407260-da850faa41e3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1487&q=80',
         caption='from url')
# generate a random image
st.image(np.random.rand(250, 250), caption='Random Image from numpy')
st.markdown('---')

st.markdown('### Audio&Video')
st.audio('https://upload.wikimedia.org/wikipedia/commons/c/c4/Muriel-Nguyen-Xuan-Chopin-valse-opus64-1.ogg')
st.video('https://pixabay.com/en/videos/star-long-exposure-starry-sky-sky-6962/')
st.markdown('---')

import time
st.markdown('### Display progress and status')
progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=progress_text)
time.sleep(1)
my_bar.empty()

with st.spinner('Wait for it...'):
    time.sleep(3)
st.success('Done!')

with st.status("Downloading data..."):
    st.write("Searching for data...")
    time.sleep(2)
    st.write("Found URL.")
    time.sleep(1)
    st.write("Downloading data...")
    time.sleep(1)

st.button('Rerun')

st.info('You can display status information with those alters', icon="ℹ️")
st.warning('This is a warning', icon="⚠️")