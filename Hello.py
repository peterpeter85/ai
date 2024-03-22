import streamlit as st
from streamlit_chat import message
import qrcode
import textwrap
import time
import os
from PIL import Image
from spellchecker import SpellChecker

def check(text):
    # 맞춤법 검사기 객체 생성
    spell = SpellChecker()
    # 문장을 단어 단위로 분할하여 잘못된 단어를 찾음
    words = text.split()
    misspelled = spell.unknown(words)
    # 잘못된 단어를 교정하여 교정된 문장을 생성
    corrected_text = ''
    for word in words:
        if word in misspelled:
            corrected_text += spell.correction(word) + ' '
        else:
            corrected_text += word + ' '
    return corrected_text.strip()
with st.sidebar:
    # Streamlit app title
    st.sidebar.title("Chatchat's logo")
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    im=Image.open("large.png")
    st.sidebar.image(im, width=250, caption="chatchat's logo")

  


with st.form("you:", clear_on_submit=True):
  user=st.text_input("")
  submitted=st.form_submit_button("✅")
if submitted and user:
  user=check(user)
  message(user,is_user=True)
  if check("넌")and check("이름이")and check("뭐야")in user.lower():
    message("안녕하세요.저는 챗챗입니다.무엇을 도와드릴까요?")
  elif check("날씨 알려줘")in user.lower():
      message("이 기능은 미완성입니다".)
  else:
    message("This comand is not on my database.Try again.")
  

