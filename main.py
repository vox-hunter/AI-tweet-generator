from fetch import fetch
import streamlit as st
import time
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import os

# Load the config.yaml file
config_path = 'config.yaml'

# Read the YAML file
if os.path.exists(config_path):
    with open(config_path) as file:
        config = yaml.load(file, Loader=SafeLoader)
else:
    st.error("Configuration file not found. Please check the path.")

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['pre-authorized']
)

# Authentication
if 'authentication_status' not in st.session_state:
    st.session_state['authentication_status'] = None

if st.session_state['authentication_status'] is None:
    name, authentication_status, username = authenticator.login("main")
    register = st.button("Register")
    if register:
        st.title("User Registration")
        try:
            email, username, name = authenticator.register_user(pre_authorization=False)
            if email:
                st.success('User registered successfully')
                # Save the updated configuration file
                with open('config.yaml', 'w') as file:
                    yaml.dump(config, file, default_flow_style=False)
                st.experimental_rerun()
        except Exception as e:
            st.error(e)

    if authentication_status:
        st.session_state['authentication_status'] = True
        st.session_state['name'] = name
        st.session_state['username'] = username
        st.experimental_rerun()
    elif authentication_status is False:
        st.error('Username/password is incorrect')
    else:
        st.warning('Please enter your username and password')


# Show the main app only if authenticated
if st.session_state['authentication_status']:
    st.write(f'Welcome *{st.session_state["name"]}*')
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
    
    authenticator.logout("Logout")
