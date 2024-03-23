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
if id in ["public user"]and password in ["public user"]:
    with st.form("you:", clear_on_submit=True):
        user=st.text_input("")
        submitted=st.form_submit_button("✅")
    if submitted and user:
        message(user,is_user=True)
        if "넌"and"누구야"in user:
            message("안녕하세요.저는 챗챗입니다.무엇을 도와드릴까요")
        elif "넌"and"이름이"and"뭐야" in user:
            message("안녕하세요.저는 챗챗입니다.무엇을 도와드릴까요")
        elif "너"and"의"and"이름을"and"알고"and"싶어"in user:
            message("안녕하세요.저는 챗챗입니다.무엇을 도와드릴까요?")
        elif "넌"and"대체"and"누구야" in user:
            message("안녕하세요.저는 챗챗입니다.무엇을 도와드릴까요?")
        elif "안녕"== user:
            message("네 안녕하세요.")
        elif "너"and"의"and"로고"and"를"and"보여줘" in user:
            message("네 몰론이죠!")
            st.image(Image.open("large.png"))
        elif "신나는"and"노래"and"틀어줘"and ""in user:
            message("네 신나는 노래를 틀어드리겠습니다.아래는 노래 재생버튼 입나다.")
            st.audio("r.mp3", format="audio/mp3")
            st.audio("a.mp3", format="audio/mp3")
            st.audio("b.mp3", format="audio/mp3")
        elif "고양이"and"영상을"and"틀어줘"in user:
            message("네 고양이 영상을를 틀어드리겠습니다.아래는 영상 재생버튼 입나다.")
            st.video("https://www.youtube.com/shorts/1t7Adam0-y0", format="video/mp4")
            st.video("https://www.youtube.com/shorts/PMBrH57XDZw", format="video/mp4")
            st.video("https://www.youtube.com/shorts/JcXNnc3ygsU", format="video/mp4")
        else:
            message("This comand is not on my database.Try again.")
if id in ["tiger1234@mylittlechatchat.streamlit.app"] and password in ["tiger1234"]:
    with st.form("you:", clear_on_submit=True):
        user=st.text_input("")
        submitted=st.form_submit_button("✅")
    if submitted and user:
        message(user,is_user=True)
        if "넌"and"누구야"in user:
            message("안녕하세요.저는 챗챗입니다.무엇을 도와드릴까요")
        elif "넌"and"이름이"and"뭐야" in user:
            message("안녕하세요.저는 챗챗입니다.무엇을 도와드릴까요")
        elif "너"and"의"and"이름을"and"알고"and"싶어"in user:
            message("안녕하세요.저는 챗챗입니다.무엇을 도와드릴까요?")
        elif "넌"and"대체"and"누구야" in user:
            message("안녕하세요.저는 챗챗입니다.무엇을 도와드릴까요?")
        elif "안녕"== user:
            message("네 안녕하세요.")
        elif "너"and"의"and"로고"and"를"and"보여줘" in user:
            message("네 몰론이죠!")
            st.image(Image.open("large.png"))
        elif "신나는"and"노래를"and"틀어줘"in user:
            message("네 신나는 노래를 틀어드리겠습니다.아래는 노래 재생버튼 입나다.")
            st.audio("r.mp3", format="audio/mp3")
            st.audio("a.mp3", format="audio/mp3")
            st.audio("b.mp3", format="audio/mp3")
        elif "고양이"and"영상을"and"틀어줘"in user:
            message("네 고양이 영상을를 틀어드리겠습니다.아래는 영상 재생버튼 입나다.")
            st.video("https://www.youtube.com/shorts/1t7Adam0-y0", format="video/mp4")
            st.video("https://www.youtube.com/shorts/PMBrH57XDZw", format="video/mp4")
            st.video("https://www.youtube.com/shorts/JcXNnc3ygsU", format="video/mp4")
        else:
            message("This comand is not on my database.Try again.")
  
if id in ["peterpeter85@mylittlechatchat.streamlit.app"] and password in ["https://mylittlechatchat.streamlit.app"]:
    with st.form("you:", clear_on_submit=True):
        user=st.text_input("")
        submitted=st.form_submit_button("✅")
    if submitted and user:
        message(user,is_user=True)
        if "넌"and"누구야"in user:
            message("안녕하세요.저는 챗챗입니다.무엇을 도와드릴까요")
        elif "넌"and"이름이"and"뭐야" in user:
            message("안녕하세요.저는 챗챗입니다.무엇을 도와드릴까요")
        elif "너"and"의"and"이름을"and"알고"and"싶어"in user:
            message("안녕하세요.저는 챗챗입니다.무엇을 도와드릴까요?")
        elif "넌"and"대체"and"누구야" in user:
            message("안녕하세요.저는 챗챗입니다.무엇을 도와드릴까요?")
        elif "안녕"== user:
            message("네 안녕하세요.")
        elif "너"and"의"and"로고"and"를"and"보여줘" in user:
            message("네 몰론이죠!")
            st.image(Image.open("large.png"))
        elif "신나는"and"노래를"and"틀어줘":
            message("네 신나는 노래를 틀어드리겠습니다.아래는 노래 재생버튼 입나다.")
            st.audio("r.mp3", format="audio/mp3")
            st.audio("a.mp3", format="audio/mp3")
            st.audio("b.mp3", format="audio/mp3")
        elif "고양이"and"영상을"and"틀어줘"in user:
            message("네 고양이 영상을를 틀어드리겠습니다.아래는 영상 재생버튼 입나다.")
            st.video("https://www.youtube.com/shorts/1t7Adam0-y0", format="video/mp4")
            st.video("https://www.youtube.com/shorts/PMBrH57XDZw", format="video/mp4")
            st.video("https://www.youtube.com/shorts/JcXNnc3ygsU", format="video/mp4")
        else:
            message("This comand is not on my database.Try again.")


  

