import streamlit as st

st.title('Vi du expander')

with st.expander('Day la noi dung chi tiet san pham 1',True): #expander = False => dong chi tiet, True => mo san khi tai trang web
    st.header('San pham A')
    st.write('San pham phan khuc cao cap')
    st.image('https://picsum.photos/200/200','Anh minh hoa',200)
