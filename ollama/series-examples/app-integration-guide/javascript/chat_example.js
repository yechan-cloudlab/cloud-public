import ollama from "ollama";

const response = await ollama.chat({
  model: "gemma3",
  messages: [
    {
      role: "user",
      content: "Explain why local LLMs are useful for developers in two sentences.",
    },
  ],
});

console.log(response.message.content);
