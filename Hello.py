import streamlit as st
from streamlit_chat import message
import qrcode
import textwrap
import time
import os
from PIL import Image
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
  elif "make"and"me"and"a"and"python"and"code"and"that"or "give"and"me"and"an"and"example"and"of"and"a"and"python"and"code"in user.lower():
      message("This is not ready yet.")
  else:
    message("This comand is not on my database.Try again.")
  

