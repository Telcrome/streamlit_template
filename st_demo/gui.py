import numpy as np
import streamlit as st
import skimage.data as skdata
import time

img = skdata.astronaut()

arr = np.random.random(5)

st.image(img)

@st.cache
def get_data() -> np.ndarray:
    time.sleep(5)
    return np.random.random(5)

st.write(get_data())

st.write('changed something')

st.write(arr)

if st.button('click me'):
    st.write('hello world')
else:
    st.write('another example')
