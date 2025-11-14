import streamlit as st
#component = control streamlit

#mot container chua nhieu components
st.title("Demo container")

with st.container():
    st.write('Noi dung container')
    btn = st.button('Noi dung chi tiet')

st.markdown('<hr />',True) ####dong ke nganh

with st.container():
    st.header('Container 2')
