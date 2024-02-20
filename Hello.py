import streamlit as st
from streamlit_chat import message
import qrcode
import textwrap
import time
with st.sidebar:
  st.header("hello")
  u=st.text_input("hello")
message("hello!", is_user=True)
time.sleep(5)
message("hello!")
