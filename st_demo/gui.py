import numpy as np
import streamlit as st

arr = np.random.random(5)

st.write(arr)

if st.button('click me'):
    st.write('hello world')
else:
    st.write('another example')
