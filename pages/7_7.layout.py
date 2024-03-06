import streamlit as st

with st.sidebar:
    st.write('Content added only for this page:')
    st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )


st.write('Columns are useful for laying out content')
col1, col2, col3 = st.columns([1, 2, 3])
with col1:
   st.header("A cat with width 1")
   st.image("https://static.streamlit.io/examples/cat.jpg")
with col2:
   st.header("A dog with width 2")
   st.image("https://static.streamlit.io/examples/dog.jpg")
with col3:
   st.header("An owl with width 3")
   st.image("https://static.streamlit.io/examples/owl.jpg")
   

st.write('---')
st.write('Tabs are useful for organizing content')
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)


st.write('---')
st.write('Expander is useful for hiding less important content')
with st.expander("See explanation"):
    st.write("Explanation content goes here")
    st.image("https://static.streamlit.io/examples/dice.jpg")


st.write('---')
st.write('Forms are useful for gathering user input')
with st.form("my_form"):
   st.write("Inside the form")
   slider_val = st.slider("Form slider")
   checkbox_val = st.checkbox("Form checkbox")
   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("slider", slider_val, "checkbox", checkbox_val)


st.write('---')
st.write("There are more layout options available in the Streamlit documentation, such as containers.")

st.write(st.session_state.y)
