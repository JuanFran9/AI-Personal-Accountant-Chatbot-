from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)


# from dotenv import load_dotenv
# import openai
# import os

# # Load the .env file's variables into the environment
# load_dotenv()

# # Retrieve the API key from the environment variables
# api_key = os.getenv('OPENAI_API_KEY')
# if not api_key:
#     raise ValueError("No OpenAI API key found in environment variables")

# # Create an OpenAI client with the API key
# client = openai.OpenAI(api_key=api_key)

# # Make the completion request
# completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     ]
# )

# # Print the completion
# print(completion.choices[0].message.content)
