import streamlit as st
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from streamlit_chat import message
import qrcode
import textwrap
import time
import os
from PIL import Image
with st.sidebar:
    # Create a ChatBot instance
    chatbot = ChatBot('StreamlitChatBot')

    # Optionally, train the chatbot with a corpus
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train('chatterbot.corpus.english')

    # Streamlit app title
    st.sidebar.title("Chatchat's logo")
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    im=Image.open("large.png")
    st.sidebar.image(im, width=250, caption="chatchat's logo")

    # Main interaction loop
    user_input = st.text_input("You: ")
    if user_input:
        bot_response = chatbot.get_response(user_input)
        st.text("Bot: " + str(bot_response))
  

if "ai" not in st.session_state:
  st.session_state["ai"]=[]
with st.form("you:", clear_on_submit=True):
  user=st.text_input("")
  submitted=st.form_submit_button("✅")
if submitted and user:

  message(user,is_user=True)
  if user=="너는 누구야?":
    message("저는 인공지능 챗봇 챗챗입니다.")
  else:
    message("등록된 명령이 아닙니다.")
  

