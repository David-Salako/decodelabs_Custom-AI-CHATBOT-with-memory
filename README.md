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

- Holds natural conversations using Google's Gemini AI.
- Remembers previous messages during the current chat session.
- Responds based on earlier parts of the conversation.
- Allows users to clear the conversation and start over.
- Prevents invalid or empty messages from being sent.

---

## Requirements

Before running the project, you'll need:

- Python 3.10 or later
- A Gemini API key from Google AI Studio

---

## Running the Project

Start the chatbot by running:

```bash
python main.py
```

When the chatbot starts, you'll see a screen like this:

```
Custom AI Chatbot with Memory

Type your message and press Enter.

Commands:
/history
/clear
/exit
```

---

## Example Conversation

**You:** My name is David.

**Chatbot:** Nice to meet you, David! How can I help you today?

**You:** What is my name?

**Chatbot:** Your name is David.

---

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


## Future Improvements

Possible enhancements include:

- Saving conversations even after the program is closed.
- Adding voice input and voice responses.
- Creating a web interface instead of using the terminal.
- Allowing users to have multiple chat sessions.
