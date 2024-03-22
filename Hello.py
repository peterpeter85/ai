import streamlit as st
from streamlit_chat import message
import qrcode
import textwrap
import time
import os
from PIL import Image
from spellchecker import SpellChecker
with st.sidebar:
    # Streamlit app title
    st.sidebar.title("Chatchat's logo")
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    im=Image.open("large.png")
    st.sidebar.image(im, width=250, caption="chatchat's logo")

import requests
import os
import json
import re

def weather(location, unit="섭씨"):
    
    reg = re.compile(r'[a-zA-Z]') # 영어 입력인지를 검사하는 정규식  
    
    if reg.match(location): # 영어로 도시 이름을 지정한 경우  
        city = location # 영어 도시 이름을 바로 지정
    else: # 영어로 지정하지 않은 경우 
        city_names = {"서울": "Seoul", "인천": "Incheon", "대전": "Daejeon", 
                      "대구": "Daegu", "부산": "Busan", "광주": "Gwangju",
                      "수원": "Suwon", "파리": "Paris", "뉴욕": "New York"}
        city = city_names[location] # 한글 도시 이름을 영어로 변경

    url = "http://api.weatherapi.com/v1/current.json"
    parameters = {"key":"dbf7e1eba47640cabf0103552242203", "q":city}

    r = requests.get(url, params=parameters)
    current_weather = r.json()
    
    name = current_weather['location']['name'] # 설정 지역
    localtime = current_weather['location']['localtime'] # 날짜 및 시각
    temp_c = current_weather['current']['temp_c'] # 섭씨 온도
    temp_f = current_weather['current']['temp_f'] # 화씨 온도
    condition_text = current_weather['current']['condition']['text'] # 날씨 상태
     
    # unit 지정에 따라서 섭씨 온도 혹은 화씨 온도를 지정
    if unit == "섭씨":
        temp = temp_c
    elif unit == "화씨":
        temp = temp_f
    else:
        unit == "섭씨"
        temp = temp_c
        
    weather_info = {
            "location": name,
            "temperature": temp,
            "unit": unit,
            "current weather": condition_text,
            "local time": localtime
    }
    
    return json.dumps(weather_info, ensure_ascii=False) # JSON 형식으로 반환  


with st.form("you:", clear_on_submit=True):
  user=st.text_input("")
  submitted=st.form_submit_button("✅")
if submitted and user:
  message(user,is_user=True)
  if "넌"and"이름이"and "뭐야"in user.lower():
    message("안녕하세요.저는 챗챗입니다.무엇을 도와드릴까요?")
  elif "날씨 알려줘"in user.lower():
      message("네, 원하는 지역을 입력해주세요.")
      ser=st.text_input("", type="password")
      if ser:
         a=weather(ser)
         message(f"현재 {ser}지역의 날씨:{a}")
  else:
    message("This comand is not on my database.Try again.")
  

