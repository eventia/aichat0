# test_01.py
# openai API 를 이용한 채팅 API 

import openai
import config

openai.api_key = config.api_key

def chat(chat_message):
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=chat_message)
    resp_dict = response.to_dict_recursive()
    assistant_turn = resp_dict['choices'][0]['message']
    return assistant_turn 

my_message = [{"role":"user", "content":"안녕하세요"}]  # {"role": "역할", "content": "내용"}
print(chat(my_message))

