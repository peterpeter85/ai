import streamlit as st
from streamlit_chat import message
import qrcode
import textwrap
import time
import os
from PIL import Image
import requests
import os
import json
import re
from spellchecker import SpellChecker
st.sidebar.title("Chatchat's logo")
os.chdir(os.path.dirname(os.path.abspath(__file__)))
im=Image.open("large.png")
st.sidebar.image(im, width=250, caption="chatchat's logo")
id=st.sidebar.text_input("USER ID:")
password=st.sidebar.text_input("USER PASSWORD:", type="password")
if id in ["tiger1234@mylittlechatchat.streamlit.app"] and password in ["tiger1234"]:
    with st.form("you:", clear_on_submit=True):
        user=st.text_input("")
        submitted=st.form_submit_button("✅")
    if submitted and user:
        message(user,is_user=True)
        if "넌"and"누구야"or "넌"and"이름이"and"뭐야" in user:
            message("안녕하세요.저는 챗챗입니다.무엇을 도와드릴까요")
         if "너"and"의"and"이름을"and"알고"and"싶어" in user:
            message("안녕하세요.저는 챗챗입니다.무엇을 도와드릴까요?")
         if "넌"and"대체"and"누구야" in user:
            message("안녕하세요.저는 챗챗입니다.무엇을 도와드릴까요?")
        elif "안녕"== user:
            message("네 안녕하세요.")
        elif "너"and"의"and"로고"and"를"and"보여줘" in user:
            message(Image.open("large.png"))
        else:
            message("This comand is not on my database.Try again.")
  
if id in ["peterpeter85@mylittlechatchat.streamlit.app"] and password in ["https://mylittlechatchat.streamlit.app"]:
    with st.form("you:", clear_on_submit=True):
        user=st.text_input("")
        submitted=st.form_submit_button("✅")
    if submitted and user:
        message(user,is_user=True)
        if "넌"and"이름이"and "뭐야"in user.lower():
            message("안녕하세요 성윤님.저는 챗챗입니다.무엇을 도와드릴까요?")
        elif "안녕"== user.lower():
            message("네 안녕하세요 성윤님.")
        else:
            message("This comand is not on my database.Try again.")
if id in ["public@mylittlechatchat.streamlit.app"] and password in ["public"]:
    with st.form("you:", clear_on_submit=True):
        user=st.text_input("")
        submitted=st.form_submit_button("✅")
    if submitted and user:
        message(user,is_user=True)
        if "넌"and"이름이"and "뭐야"in user.lower():
            message("안녕하세요.저는 챗챗입니다.무엇을 도와드릴까요?")
        elif "안녕"in user.lower():
            message("네 안녕하세요.")
        else:
            message("This comand is not on my database.Try again.")
  


  

