import streamlit as st
from streamlit_chat import message
import qrcode
import textwrap
import time
st.sidebar=st.empty()
message("hello!", is_user=True)
time.sleep(5)
message("hello!")
