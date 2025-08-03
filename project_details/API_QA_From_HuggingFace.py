import os
import requests
from dotenv import load_dotenv
load_dotenv()
API_URL = "https://router.huggingface.co/v1/chat/completions"
headers = {
    "Authorization": "",
}
# print(headers)
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
response = query({
    "messages": [
        {
            "role": "user",
            "content": "Give me python code for adding two numbers"
        }
    ],
    "model": "mistralai/Mistral-7B-Instruct-v0.2:featherless-ai"
})
print(response["choices"][0]["message"])