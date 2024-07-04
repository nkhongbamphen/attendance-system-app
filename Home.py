import streamlit as st

import face_rec

st.set_page_config(page_title='Attendance System')

st.header('Attendance System using Face Recognition')

with st.spinner('loading Models and Connecting to Redis db ...'):
    import face_rec

st.success('Model loads successfully')
st.success('Redis db successfully connected')
