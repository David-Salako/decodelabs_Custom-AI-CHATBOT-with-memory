# Custom AI Chatbot with Memory

This is the first project i built as part of my Generative AI Industrial Training at DecodeLabs.

## Overview

This is an AI-powered chatbot that can remember what you have said during a conversation.

Unlike a basic chatbot that forgets previous messages, this chatbot keeps track of the conversation so it can give more natural and relevant responses.

For example:

**You:** My name is David.

**Chatbot:** Nice to meet you, David!

A few messages later...

**You:** What is my name?

**Chatbot:** Your name is David.

The chatbot remembers earlier parts of the conversation, making the interaction feel more like talking to a real person.

---

## Features

- Session-based conversational memory for context-aware responses.
- Integration with the Google Gemini API for natural language generation.
- Input validation to prevent invalid requests.
- Built-in commands for viewing, clearing, and ending chat sessions.
- Modular architecture separating conversation management from AI communication.

## Available Commands

While chatting, you can use these commands:

- **/history** – View the conversation so far.
- **/clear** – Clear the conversation and start a new chat.
- **/exit** – Close the chatbot.

---

## Project Files

- **main.py** – Starts the chatbot.
- **gemini_client.py** – Connects the chatbot to Google's Gemini AI.
- **history_manager.py** – Stores the conversation so the chatbot can remember previous messages.
- **requirements.txt** – Lists the required Python packages.
- **README.md** – Project documentation.


## Technologies Used

- Python
- Google Gemini API
- python-dotenv
