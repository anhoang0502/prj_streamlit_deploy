import streamlit as st

#tren web chi co 1 sidebar duy nhat
#st.sidebar.widget = layout tung component trong sidebar
st.sidebar.title("Tieu de sidebar")

with st.sidebar.expander('Quan tri',True):
    selectmenu = st.radio('Menu',['Menu item 1','Menu item 2','Menu item 3'])

st.sidebar.markdown('<hr />',True) #Dong ke ngang