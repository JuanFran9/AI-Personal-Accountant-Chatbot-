import openai
from openai import OpenAI

client = OpenAI()

messages = []
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready!")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = completion.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")
