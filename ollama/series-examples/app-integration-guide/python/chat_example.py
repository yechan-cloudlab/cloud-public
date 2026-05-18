from ollama import chat

response = chat(
    model="gemma3",
    messages=[
        {
            "role": "user",
            "content": "Explain why local LLMs are useful for developers in two sentences.",
        }
    ],
)

print(response.message.content)
