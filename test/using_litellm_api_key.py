from config.env_settings import settings

import requests
import openai


TEST_API_KEY = settings.SAMPLE_API_KEY
BASE_URL = settings.BASE_URL

client = openai.OpenAI(
    api_key = TEST_API_KEY,
    base_url = BASE_URL
)

response = client.chat.completions.create(
    model="Qwen/Qwen3-8B",
    messages=[{
        "role": "user",
        "content": "인공지능에 대하여 간단하게 설명해줘."   
    }]
)

print(response.choices[0].message.content)