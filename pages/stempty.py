#tao ra mot vung trong tren giao dien => co the cap nhat du lieu sau

import streamlit as st
import time

placeholder = st.empty()


for num in range(1000):
    placeholder.write(num)
    time.sleep(1) #sau moi mot giay, cap nhat lai placeholder, tu 0 den 999