# streamlit run front_01.py

import streamlit as st
from streamlit_chat import message

message("도움이입니다")
message("유저입니다", is_user=True)