import openai

# Set your OpenAI API key
openai.api_key = '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'

# Your code to generate the prompt/question
question = "What is the capital of France?"

# Call the Completion.create function
response = openai.Completion.create(
    engine="gpt-3.5-turbo",  # Replace with the appropriate engine
    prompt=question,
    max_tokens=100  # Adjust the max_tokens as per your requirement
)

# Extract the generated answer from the response
answer = response['choices'][0]['text']
print(answer)
