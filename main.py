import streamlit as st
from streamlit_oauth import OAuth2Component
import base64
import json
from fetch import fetch
import time


# import logging
# logging.basicConfig(level=logging.INFO)

# create an OAuth2Component instance
CLIENT_ID = st.secrets["google"]["CLIENT_ID"]
CLIENT_SECRET = st.secrets["google"]["CLIENT_SECRET"]
AUTHORIZE_ENDPOINT = st.secrets["google"]["AUTHORIZE_ENDPOINT"]
TOKEN_ENDPOINT = st.secrets["google"]["TOKEN_ENDPOINT"]
REVOKE_ENDPOINT = st.secrets["google"]["REVOKE_ENDPOINT"]

if "auth" not in st.session_state:
    # create a button to start the OAuth2 flow
    oauth2 = OAuth2Component(CLIENT_ID, CLIENT_SECRET, AUTHORIZE_ENDPOINT, TOKEN_ENDPOINT, TOKEN_ENDPOINT, REVOKE_ENDPOINT)
    st.title("Tweet Generator")
    st.divider()
    st.write("Please login to continue.")
    result = oauth2.authorize_button(
        name="Continue with Google",
        icon="https://www.google.com.tw/favicon.ico",
        redirect_uri="https://tweet-generator-ai.streamlit.app/",
        scope="openid email profile",
        key="google",
        extras_params={"prompt": "consent", "access_type": "offline"},
        use_container_width=True,
        pkce='S256',
    )
    
    if result:
        st.write(result)
        # decode the id_token jwt and get the user's email address
        id_token = result["token"]["id_token"]
        # verify the signature is an optional step for security
        payload = id_token.split(".")[1]
        # add padding to the payload if needed
        payload += "=" * (-len(payload) % 4)
        payload = json.loads(base64.b64decode(payload))
        email = payload["email"]
        st.session_state["auth"] = email
        st.session_state["token"] = result["token"]
        st.rerun()
else:
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

                    st.link_button("Post Tweet", f"https://twitter.com/intent/tweet?text={tweet}")
    if st.button("Logout"):
        del st.session_state["auth"]
        del st.session_state["token"]
        st.rerun()
