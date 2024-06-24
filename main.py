from fetch import fetch
import streamlit as st
import time


st.title("Tweet Generator")
st.divider()

with st.form("tweet_form"):
    topic = st.text_input("Enter the topic of the tweet")
    mood = st.text_input("Enter the mood of the tweet")
    style = st.text_input("Enter the style of the tweet")
    generate_button = st.form_submit_button("Generate Tweet")

    if generate_button:
        with st.spinner("Generating tweet..."):
            try:
                tweet = fetch(topic, mood, style)
            except KeyError:
                st.error("An error occurred while generating the tweet. Please try again.")
            else:
                def stream_data():
                    for word in tweet.split(" "):
                        yield word + " "
                        time.sleep(0.05)  # Adjust the sleep time to control the speed of the stream
                st.success("Tweet generated!")
                st.write("".join(stream_data()))

                st.markdown(f'[Post Tweet](https://twitter.com/intent/tweet?text={tweet})')
    

