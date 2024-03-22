import streamlit as st
from streamlit_chat import message
import qrcode
import textwrap
import time
import os
from PIL import Image
from spellchecker import SpellChecker

def spell_check(text):
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

# 텍스트 입력
text = "안녕하세여. 한국어 맞춤법 검사기 테스트 입니다."
# 맞춤법 검사
checked_text = spell_check(text)
# 결과 출력
print("원본 텍스트:", text)
print("교정된 텍스트:", checked_text)

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

  message(user,is_user=True)
  if "what"and"is"and"your"and"name"in user.lower():
    message("Hello!I am Chatchat.What may I help you today?")
  elif :
      message("This is not ready yet.")
  else:
    message("This comand is not on my database.Try again.")
  

