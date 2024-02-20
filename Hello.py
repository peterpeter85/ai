import streamlit as st
from streamlit_chat import message
import qrcode
import textwrap
import time
if "past" not in st.session_state:
  st.session_state["past"]=[]
if "ai" not in st.session_state:
  st.session_state["ai"]=[]
with st.form("you:", clear_on_submit=True):
  user=st.text_input("")
  submitted=st.form_submit_button("✅")
if submitted and user:
  st.session_state.past.append(user)
  message(st.session_state.past[index],is_user=True)
  message(user,is_user=True)
  if user=="너는 누구야?":
    st.session_state.ai.append("저는 인공지능 챗봇 챗챗입니다.")
  else:
    st.session_state.ai.append("등록된 명령이 아닙니다.")
  for index, pas in enumerate(st.session_state.ai):
    message(pas)
    
    

