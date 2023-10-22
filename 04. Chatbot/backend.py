# from typing import List
# from fastapi import FastAPI
# from pydantic import BaseModel
import openai
import config

openai.api_key = config.api_key

def chat(chat_message):
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=chat_message)
    resp_dict = response.to_dict_recursive()
    assistant_turn = resp_dict['choices'][0]['message']
    return assistant_turn # {"role": "assistant", "content": "blahblahblah"}

my_message = [{"role":"user", "content":"너는 누구?"}]
print(chat(my_message))


# app = FastAPI()

# class Turn(BaseModel):
#     role: str
#     content: str

# class Messages(BaseModel):
#     messages: List[Turn]  # [{"role": "user", "content": "blahblahblah"}, {"role": "assistant", "content": "blahblahblah"}, ...]


# @app.post("/chat", response_model=Turn)
# def post_chat(messages: Messages):
#     messages = messages.dict()
#     assistant_turn = chat(messages=messages['messages'])
#     return assistant_turn
