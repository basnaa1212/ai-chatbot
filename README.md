# AI Chatbot

## Project Description

This is a simple AI chatbot built using Python and Streamlit as part of the WeIntern Week 2 assignment.

The chatbot answers predefined questions about topics such as Python, Artificial Intelligence, Machine Learning, Data Science, and Power BI.

## Technologies Used

- Python
- Streamlit
- JSON

## Features

- Simple and interactive chatbot interface
- Separate intent dataset using `intents.json`
- Predefined questions and answers
- Basic greeting and goodbye responses
- Exact phrase matching
- Multi-word pattern matching
- Single-word keyword matching
- Fallback response for unrecognized messages
- Chat history maintained during the session

## How to Run

1. Install Python.
2. Install the required packages by running:

   ```
   py -m pip install -r requirements.txt
   ```

3. Open the project folder in the terminal.
4. Run the application:

   ```
   py -m streamlit run app.py
   ```

5. Open the local URL shown in the terminal.

## Project Files

- `app.py` — chatbot source code
- `intents.json` — predefined questions and answers
- `requirements.txt` — required Python packages
- `sample_input_output.md` — sample conversations
- `README.md` — project information