#tao nhieu trang lien ket voi nhau
#trang chinh o mot noi, trang lien ket o folder page
#ten folder la page la bat buoc
import streamlit as st

st.set_page_config(layout="wide",page_title="Ung dung thong ke du lieu",menu_items={
    "About":"https://cybersoft.edu.vn"
})
st.sidebar.header('Dashboard')

with st.container():
    st.header('Home page')
    st.write('Content home page')

st.page_link('pages/sttabs.py',label='Demo tab') #tao link len page home

