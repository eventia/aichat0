# streamlit run front.py    

import streamlit as st
from streamlit_chat import message
import requests

if 'messages' not in st.session_state:
    st.session_state['messages'] = []

chat_url = "http://localhost:8000/chat"

def chat(text):
    user_turn = {"role": "user", "content": text}
    messages = st.session_state['messages']
    resp = requests.post(chat_url, json={"messages": messages + [user_turn]})
    assistant_turn = resp.json()
    
    st.session_state['messages'].append(user_turn)
    st.session_state['messages'].append(assistant_turn)

st.title("인공지능 챗봇")

input_text = st.text_input("You")
if input_text:
  chat(input_text)

for i, msg_obj in enumerate(st.session_state['messages']):
  raw_msg = msg_obj['content']
  is_user = False
  if i%2 == 0:
    is_user=True
  message(raw_msg, is_user=is_user, key=f"no_{i}")
    

