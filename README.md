# Custom AI Chatbot with Memory

DecodeLabs Generative AI Industrial Training — Project 1

A terminal chatbot that remembers the full conversation during a live
session, using Gemini as the model and a manually-managed in-memory
history arrayv to demonstrate stateful architecture explicitly.

## PREREQUISITES

Python 3.10+
A Gemini API key — this project will not run without one. Get an API key from Google AI Studio,
then follow the setup steps below to add it to a .env file.


The file you run

main.py — it imports history_manager.py and gemini_client.py, you
never run those two directly.


## Run This 

\`\`\`bash
python main.py
\`\`\`
## This is what the terminal looks like 
╭───────────────────────────────────────────╮
│ Custom AI Chatbot with Memory              │
│ DecodeLabs GenAI Industrial Training       │
│                                             │
│ Type your message and press Enter.         │
│ Commands: /history  /clear  /exit          │
╰───────────────────────────────────────────╯

You: My name is David
Gemini:
Nice to meet you, David! How can I help you today?
(2 turns in memory)

You: What is my name?
Gemini:
Your name is David.
(4 turns in memory)



## What this project demonstrates

- Stateful architecture: every turn appends to a ChatHistory array
  ('history_manager.py') and the entire array is resent to Gemini on
  each call — turning a stateless API into a contextual conversation.
- Structural validation gate: empty/whitespace input is rejected
  locally before it ever reaches the API, preventing a 400 crash.
- Sliding window (FIFO) pruning: once the history exceeds 20 turns,
  the oldest ones are dropped automatically, protecting against context
  window overflow on long sessions.

## Commands inside the chat

- `/history` — print the full in-memory conversation array
- `/clear` — wipe the session and start fresh
- `/exit` — quit
