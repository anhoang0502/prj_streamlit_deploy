import streamlit as st
st.set_page_config(layout='wide')
# col1, col2 = st.columns(2)

# with col1:
#     st.title('MENU KFC MINI')
#     st.subheader('Chon mon an:')
#     st.write('Ga ran (35_000 VND)')
#     garan = st.number_input(placeholder='nhap so luong ga ran')
#     st.write('Burger bo (45_000 VND)')
#     burger = st.number_input(placeholder='nhap so luong burger bo')
#     st.write('Khoai tay chien (25_000 VND)')
#     khoai = st.number_input(placeholder='nhap so luong khoai tay chien')
#     st.write('Pepsi (15_000 VND)')
#     pepsi = st.number_input(placeholder='nhap so luong pepsi')
#     st.write('Kem vani (20_000 VND)')
#     kem = st.number_input(placeholder='nhap so luong kem vani')
#     st.markdown('<hr / >',True)
#     st.write('Nhap so luong mon ban muon mua')
# with col2:
#     table=[
#     {"HCM":1_000_000_000},
#     {"HN":500_000_000},
#     {"DN":300_000_000}
#     ]

# st.table(data=table)

#du lieu cac mon an (st.session_state.lst_mon_an)
if "lst_mon_an" not in st.session_state:
    st.session_state.lst_mon_an = []

st.title('MENU KFC MINI')

dict_gia={
    "garan":35000,
    "bo":45000,
    "khoai":25000,
    "pepsi":15000,
    "kem":20000
}
dict_chon={
    "garan":1,
    "bo":1,
    "khoai":1,
    "pepsi":1,
    "kem":1
}

col1, col2 = st.columns(2)
with col1:
    form_mon_an = st.form("From mon an")
    with form_mon_an:
        st.title('Chon mon an:')
        dict_chon['garan'] = st.number_input('Ga ran (35,000 VND)',max_value=10, min_value=1, step=1,value=1,placeholder='nhap so luong ga ran')
        dict_chon['bo'] = st.number_input('Burger bo (45,000 VND)',max_value=10, min_value=1, step=1,value=1,placeholder='nhap so luong burger bo')
        dict_chon['khoai'] = st.number_input('Khoai tay chien (25,000 VND)',max_value=10, min_value=1, step=1,value=1,placeholder='nhap so luong khoai tay chien')
        dict_chon['pepsi'] = st.number_input('Pepsi (15,000 VND)',max_value=10, min_value=1, step=1,value=1,placeholder='nhap so luong pepsi')
        dict_chon['kem'] = st.number_input('Kem vani (20,000 VND)',max_value=10, min_value=1, step=1,value=1,placeholder='nhap so luong kem vani')
        st.markdown('<hr / >',True)
        st.write('Nhap so luong mon ban muon mua')        
        btn = form_mon_an.form_submit_button('Dat mon')

with col2:
    st.title('Hoa don cua ban:')
    lstmonan=[]
    for key in dict_chon:
        lstmonan.append({
            'Mon an':key,
            'Don gia':dict_gia[key],
            'So luong':dict_chon[key],
            'Thanh tien': dict_gia[key]*dict_chon[key]
        })
    st.table(lstmonan)

    tongtien = 0
    for item in lstmonan:
        tongtien +=item['Thanh tien']
    st.subheader(f'Tong hoa don: {tongtien}')
