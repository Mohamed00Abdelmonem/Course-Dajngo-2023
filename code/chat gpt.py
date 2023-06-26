# import openai
# openai.api_key = "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"


# def ask_gpt(prompt):
#     completions = openai.Completion.create(
#         engine="davinci",
#         prompt=prompt,
#         max_tokens=1024,
#         n=1,
#         stop=None,
#         temperature=0.5,
#     )
#     message = completions.choices[0].text.strip()
#     return message

# while True:
#     user_input = input("You: ")
#     if user_input.lower() in ['exit', 'quit', 'bye']:
#         print("Chatbot: Goodbye!")
#         break
#     response = ask_gpt(f"You: {user_input}\nChatbot:")
#     print("Chatbot:", response)



# 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




import openai

openai.api_key = "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"


response = openai.Completion.create(
    model="text-davinci-003",
    prompt="hello , how are you feleling",
    temperature=0.3,
    max_tokens=1000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
)
print(response)