# Import the necessary modules from the openai and gradio packages
import openai
import gradio

# Initialize the OpenAI client. Note that this line is not necessary if you're using the openai library directly
# as shown in the response = openai.ChatCompletion.create(...) line.
client = OpenAI()

# Create a list of messages with an initial system message that sets the context for the ChatGPT model.
messages = [{"role": "system", "content": "You are professional accountant"}]

# Define the function that will handle the conversation with the ChatGPT model.
def CustomChatGPT(user_input):
    # Append the user's message to the conversation history.
    messages.append({"role": "user", "content": user_input})

    # Make a call to the OpenAI API to generate a chat completion based on the current conversation history.
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",  # Specify the model to use.
        messages=messages  # Pass the conversation history.
    )

    # Extract the assistant's reply from the response.
    ChatGPT_reply = response.choices[0].message.content

    # Append the assistant's reply to the conversation history.
    messages.append({"role": "assistant", "content": ChatGPT_reply})

    # Return the assistant's reply for the interface to display.
    return ChatGPT_reply

# The interface uses the CustomChatGPT function to process user input and generate replies.
demo = gradio.Interface(fn=CustomChatGPT, inputs="text", outputs="text", title="AI Personal Accountant ChatBot")


# Launch the Gradio app, making it accessible via a public link.
# The 'share=True' parameter makes the interface available on the internet through Gradio's sharing feature.
demo.launch(share=True)
