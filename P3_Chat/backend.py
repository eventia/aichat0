# uvicorn backend:app --reload

from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
import openai

openai.api_key = "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"


def chat(messages):
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    resp_dict = response.to_dict_recursive()
    assistant_turn = resp_dict['choices'][0]['message']
    return assistant_turn # {"role": "assistant", "content": "blahblahblah"}

app = FastAPI()

class Turn(BaseModel):
    role: str
    content: str

class Messages(BaseModel):
    messages: List[Turn]  # [{"role": "user", "content": "blahblahblah"}, {"role": "assistant", "content": "blahblahblah"}, ...]


@app.post("/chat", response_model=Turn)
def post_chat(messages: Messages):
    messages = messages.dict()
    assistant_turn = chat(messages=messages['messages'])
    return assistant_turn
