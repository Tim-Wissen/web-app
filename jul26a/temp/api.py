import openai
import tkinter as tk
import threading

# Function to handle the user button press and process the text
def process_input():
    user_text = entry.get()  # Get the user's input from the entry widget

    # Function to make the API call in a separate thread
    def call_openai_api():
        # Call the Completion.create function
        response = openai.Completion.create(
            engine="text-davinci-002",  # Replace with the appropriate engine
            prompt=user_text,
            max_tokens=100  # Adjust the max_tokens as per your requirement
        )

        # Extract the generated answer from the response
        answer = response['choices'][0]['text']
        print(answer)

    # Start the API call in a new thread
    threading.Thread(target=call_openai_api).start()

# Set your OpenAI API key securely (using environment variable, for example)
openai.api_key = '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'

window = tk.Tk()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Output", command=process_input)
button.pack()

window.mainloop()
