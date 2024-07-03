import os
import google.generativeai as genai
import streamlit as st


# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
API_KEY = st.secrets["general"]["api_key"]
genai.configure(api_key=API_KEY)
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

def fetch(topic, mood, style, limit=280):
  response = model.generate_content(
    f"input: Generate a tweet no more than {limit} characters. (includes spaces)\nTopic of the tweet : {topic}\nMood: {mood}\nTweet style: Like {style}"
  )
  if len(response.text) > 280:
    response = model.generate_content(
      f"input: Generate a tweet no more than {limit} characters. (includes spaces)\nTopic of the tweet : {topic}\nMood: {mood}\nTweet style: Like {style}"
    )
  return response.text

def main():
    topic = input("Enter the topic of the tweet: ")
    mood = input("Enter the mood of the tweet: ")
    style = input("Enter the style of the tweet: ")
    tweet = fetch(topic, mood, style)
    print(tweet)

if __name__ == "__main__":
    main()