from __future__ import annotations

from sonar_client import create_completion

messages = [
    {
        "role": "system",
        "content": "You are a concise research assistant. Answer in Korean.",
    },
    {
        "role": "user",
        "content": "Summarize three differences between Perplexity Sonar API and a general LLM API.",
    },
]

completion = create_completion(messages)
print(completion.choices[0].message.content)
