import streamlit as st

#Markdown
st.markdown("""
    <style>
        [data-testid = "stSidebarNav"] {
            dispplay: none;
        }
    </style>
""",unsafe_allow_html=True)


#Content
st.set_page_config(layout="wide",page_title = 'Dashboard')

st.title('Admin Dashboard')

with st.container():
    col1,col2,col3,col4 = st.columns(4)

    with col1:
        st.metric('Doanh thu hom nay',"VND 12.5M","+5%") 

    with col2:
        st.metric('Nguoi dung moi',"327","+12%") 


    with col3:
        st.metric('Don hang',"142","-3%") 
    with col4:
        st.metric('Ti le chuyen doi',"3,8%","+0,4%")

st.markdown('<hr />',True) 

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('Doanh thu 7 ngay gan nhat')
        # lstx = [6,14,5,14,12,10,9]
        # lsty = [1,2,3,4,5,6,7]
        data = [6,14,5,14,12,10,9]
        st.line_chart(data=data)
    with col2:
        st.subheader('So luong don theo trang thai')
        # lstx = [6,14,5,14,12,10,9]
        # lsty = [1,2,3,4,5,6,7]
        data = [15,35,53,15]
        st.bar_chart(data=data)

#Sidebar
st.sidebar.header('Menu')
st.sidebar.header('Menu- Admin')
st.sidebar.page_link('D:/CS/buoi_8/baitap/app.py',label='Dieu huong') 
st.sidebar.page_link('D:/CS/buoi_8/baitap/pages/baocao.py',label='Bao cao') 
st.sidebar.page_link('D:/CS/buoi_8/baitap/pages/nguoidung.py',label='Nguoi dung') 
st.sidebar.page_link('D:/CS/buoi_8/baitap/pages/caidat.py',label='Cai dat')
st.sidebar.page_link('D:/CS/buoi_8/baitap/pages/btmenu.py',label='Bai tap Menu')
 

