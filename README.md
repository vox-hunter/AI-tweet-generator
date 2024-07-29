# Tweet Generator

This is a Python-based application that generates tweets based on user input. It uses the Streamlit library to create a web-based user interface.

## Getting Started
You can view my live site [here](https://tweet-generator-ai.streamlit.app/)

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have Python installed on your machine. You can download Python from [here](https://www.python.org/downloads/). This project also requires the following Python libraries:

- Streamlit
- fetch (a custom module in this project)

You can install these packages using pip:

```bash
pip install -r requirements.txt
```

### Running the Application

To run the application, navigate to the project directory in your terminal and run the following command:

```bash
streamlit run main.py
```

## Using the Tweet Generator

The Tweet Generator has three input fields:

- Topic: Enter the topic of the tweet.
- Mood: Enter the mood of the tweet.
- Style: Enter the style of the tweet.
- If you are a X premium user, make sure to toggle the premium limit. It changes the tweet limit from 280 characters to 25,000 characters
- To generate a tweet in different language, fill the input field in the language you desire.

After filling in these fields, click the "Generate Tweet" button. The application will generate a tweet based on your inputs and display it on the screen. You can then post the generated tweet to Twitter by clicking the "Post Tweet" button.

## Contributing

Please read [CONTRIBUTING.md](https://github.com/vox-hunter/AI-Tweet-Generator/blob/main/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/vox-hunter/AI-Tweet-Generator/blob/main/LICENSE) file for details

## Credits
- [Vox](https://github.com/vox-hunter)
- Gemini 1.5 Flash LLM
- Streamlit for deploying