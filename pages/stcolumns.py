#st.columns(n): chia giao dien thanh n cot
#Ctrl C => tat server web
import streamlit as st


#chinh bo cuc layout full page
st.set_page_config(layout="wide")

#boc tach goi column tu tuple (hoac goi bang cach ten_tuple[index])
col1,col2,col3,col4,col5,col6 = st.columns(6) # => tra ve tuple co (col1, col2, ...., col6)


with col1:
    st.header('Day la noi dung cot 1')
    st.subheader('Chi tiet so lieu don hang')
    st.metric('So lieu don hang',"1500 don","+5%") #cuc thong ke so lieu


with col2:
    st.header('Day la noi dung cot 2')
    st.subheader('So luot truy cap')
    st.metric('Luot truy cap',"1 200 000 luot","-5%") #cuc thong ke so lieu

with col3:
    st.header('Day la noi dung cot 3')
    st.subheader('Khach hang moi')
    st.metric('Khach hang moi',"300","20%") #cuc thong ke so lieu