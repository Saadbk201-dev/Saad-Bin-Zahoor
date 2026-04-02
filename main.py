from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

# Check if key is loading correctly
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    print("ERROR: GROQ_API_KEY not found in .env file!")
    exit()

print(f"Key loaded: {api_key[:8]}...")  # shows first 8 chars only

client = Groq(api_key=api_key)

chat_history = [
    {
        "role": "system",
        "content": "You are a helpful AI assistant."
    }
]

print("Chatbot ready! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if not user_input.strip():  # ignore empty enters
        continue

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    chat_history.append({
        "role": "user",
        "content": user_input
    })

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=chat_history
        )
        reply = response.choices[0].message.content
        chat_history.append({
            "role": "assistant",
            "content": reply
        })
        print(f"\nBot: {reply}\n")

    except Exception as e:
        print(f"\nERROR: {e}\n")