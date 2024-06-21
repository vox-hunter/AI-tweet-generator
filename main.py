from fetch import fetch
import streamlit as st

st.title("Tweet Generator")

with st.form("tweet_form"):
    topic = st.text_input("Enter the topic of the tweet")
    mood = st.text_input("Enter the mood of the tweet")
    style = st.text_input("Enter the style of the tweet")
    generate_button = st.form_submit_button("Generate Tweet")

if generate_button:
    tweet = fetch(topic, mood, style)
    st.write(tweet)
