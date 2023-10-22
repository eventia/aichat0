# test_04.py
# uvicorn test_04:app --reload

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

class Message(BaseModel):
    role: str
    content: str

class Messages(BaseModel):
    messages: List[Message]  # [{"role": "user", "content": "blahblahblah"}, {"role": "assistant", "content": "blahblahblah"}, ...]

@app.post("/chat", response_model=Message)
def post_chat(request_body: Messages):
    message_list  = request_body.model_dump()
    # message_list  = request_body.dict()
    assistant_turn = chat(chat_message=message_list['messages'])
    return assistant_turn
