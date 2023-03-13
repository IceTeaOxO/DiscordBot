import os
import openai
from dotenv import load_dotenv

load_dotenv()


openai.api_key = os.getenv("OPENAI_API_KEY")

def imageAPI(input_text):
  response = openai.Image.create(
    prompt=input_text,
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  # print(image_url)
  return image_url

def chatAPI(input_text):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=input_text,
    temperature=0.9,
    max_tokens=1500,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
  )
  text = response["choices"][0]["text"]
  return text
# print(response)
# text = response["choices"][0]["text"]
# print(text)