# Chat Bot

This is a simple chat bot implemented in Python. It uses a knowledge base stored in a JSON file to answer user questions. If it doesn't know the answer to a question, it asks the user to teach it.

## Features

- Load and save the knowledge base from/to a JSON file.
- Find the best match for a user's question from the knowledge base using the `difflib` library.
- Learn new responses from the user.

## How to Use

1. Run the script in a Python environment.
2. The chat bot will ask you questions. Type your question and press Enter.
3. If the bot knows the answer, it will respond. If not, it will ask you to teach it.
4. To teach the bot a new response, type the answer and press Enter. If you don't want to teach the bot, type 'skip' and press Enter.
5. To quit the chat, type 'quit' and press Enter.

## Code Structure

- `load_knowledge_base(file_path: str) -> dict`: Load the knowledge base from a JSON file.
- `save_knowledge_base(file_path: str, data: dict)`: Save the knowledge base to a JSON file.
- `find_best_match(user_question: str, question: list[str]) -> str | None`: Find the best match for a user's question from a list of questions.
- `get_answer_for_question(question: str, knowledge_base: dict) -> str | None`: Get the answer for a question from the knowledge base.
- `chat_bot()`: Run the chat bot.

## Dependencies

- Python 3.8+
- difflib
- json
