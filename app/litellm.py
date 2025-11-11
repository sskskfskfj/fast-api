from litellm import completion
from config.env_settings import settings

import os


os.environ["HUGGINGFACE_API_KEY"] = settings.HUGGINGFACE_API_KEY
os.environ["UI_USERNAME"] = settings.UI_USERNAME
os.environ["UI_PASSWORD"] = settings.UI_PASSWORD
os.environ["DATABASE_URL"] = settings.DATABASE_URL

def get_response(message):
    response = completion(
        model = "huggingface/Qwen/Qwen3-8B",
        messages = [{
            "content" : message,
            "role" : "user"
        }],
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    response = get_response("오늘 날씨가 어떄")
    print(response)