#tab giong column => nhung khong cung tren 1 giao dien, chia thanh nhieu tab giao dien

#truyen vao tab mot list = > tra ve tuple so tab theo so ptu lst

import streamlit as st
tabgt, tabbd, tabdl = st.tabs(['Gioi thieu','Bieu do', 'Du lieu'])

with tabgt:
    st.write('Gioi thieu ve san pham xyz:')
    st.image('https://picsum.photos/200/200','Anh minh hoa',700)

with tabbd:
    lstdoanhthu = [100_000_000,200_000_000,300_000_000,400_000_000]
    st.write('Doanh thu theo quy')
    st.area_chart(lstdoanhthu)

with tabdl:
    st.write('Du lieu doanh thu')
    st.table(lstdoanhthu)
    #edit_data la mot lst khac
    edit_data = st.data_editor(lstdoanhthu, num_rows=True) #table edit duoc truc tiep tren giao dien
    print(edit_data)
