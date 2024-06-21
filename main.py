from fetch import fetch
import streamlit as st

st.title("Tweet Generator")
topic = st.text_input("Enter the topic of the tweet")
mood = st.text_input("Enter the mood of the tweet")
style = st.text_input("Enter the style of the tweet")
if st.button("Generate Tweet"):
    tweet = fetch(topic, mood, style)
    st.write(tweet)
