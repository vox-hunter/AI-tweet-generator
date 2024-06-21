from fetch import fetch
import streamlit as st

st.title("Tweet Generator")

with st.form("tweet_form"):
    topic = st.text_input("Enter the topic of the tweet")
    mood = st.text_input("Enter the mood of the tweet")
    style = st.text_input("Enter the style of the tweet")
    generate_button = st.form_submit_button("Generate Tweet")

if generate_button:
    with st.spinner("Generating tweet..."):
        tweet = fetch(topic, mood, style)
        st.success("Tweet generated!")
        st.write(tweet)
