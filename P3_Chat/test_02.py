# test_02.py

from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
import openai
import config

openai.api_key = config.api_key

def chat(chat_message):
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=chat_message)
    resp_dict = response.to_dict_recursive()
    assistant_turn = resp_dict['choices'][0]['message']
    return assistant_turn 


app = FastAPI()

class Turn(BaseModel):
    role: str
    content: str

class Messages(BaseModel):
    messages: List[Turn]  # [{"role": "user", "content": "blahblahblah"}, {"role": "assistant", "content": "blahblahblah"}, ...]

@app.post("/mchat", response_model=Turn)
def post_chat(request_body: Messages):
    message_list  = request_body.dict()
    assistant_turn = chat(chat_message=message_list['messages'])
    return assistant_turn
