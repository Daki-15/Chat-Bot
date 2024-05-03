import json
from difflib import get_close_matches

# Function to load the knowledge base from a JSON file
def load_knowledge_base(file_path: str) -> dict:
    # Open the file in read mode
    with open(file_path, "r") as file:
        # Load the JSON data into a Python dictionary
        data: dict = json.load(file)
    # Return the loaded data
    return data

# Function to save the knowledge base to a JSON file
def save_knowledge_base(file_path: str, data: dict):
    # Open the file in write mode
    with open(file_path, "w") as file:
        # Dump the Python dictionary into the file as JSON
        json.dump(data, file, indent = 2)

# Function to find the best match for a user's question from a list of questions
def find_best_match(user_question: str, question: list[str]) -> str | None:
    # Get the close matches for the user's question from the list of questions
    matches: list = get_close_matches(user_question, question, n=1, cutoff=0.6)
    # Return the first match if there are any matches, otherwise return None
    return matches[0] if matches else None

# Function to get the answer for a question from the knowledge base
def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    # Iterate over the questions in the knowledge base
    for q in knowledge_base['questions']:
        # If the current question matches the input question
        if q['question'] == question:
            # Return the answer for the current question
            return q["answer"]

# Function to run the chat bot
def chat_bot():
    # Load the knowledge base
    knowledge_base: dict = load_knowledge_base("./knowledge_base.json")
    
    # Run the chat bot in a loop
    while True:
        # Get the user's input
        user_input = input("You: ")

        # If the user's input is 'quit', break the loop
        if user_input.lower() == 'quit':
            break

        # Find the best match for the user's input from the questions in the knowledge base
        best_match: str | None = find_best_match(user_input, [q['question'] for q in knowledge_base['questions']]) 

        # If there is a best match
        if best_match:
            # Get the answer for the best match
            answer: str = get_answer_for_question(best_match, knowledge_base)
            # Print the answer
            print(f"Bot: {answer}")
        else:
            # If there is no best match, ask the user to teach the bot
            print("Bot: I don't know the answer. Can you teach me?")
            # Get the new answer from the user
            new_answer: str = input("Type the answer or 'skip' to skip: ")

            # If the new answer is not 'skip'
            if new_answer.lower() != 'skip':
                # Add the new question and answer to the knowledge base
                knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
                # Save the updated knowledge base
                save_knowledge_base('./knowledge_base.json', knowledge_base)
                # Thank the user for teaching the bot
                print("Bot: Thank you! I learned a new response.")

# Run the chat bot if this script is the main module
if __name__ == "__main__":
    chat_bot()
