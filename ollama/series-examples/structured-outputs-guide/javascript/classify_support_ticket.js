import ollama from "ollama";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const SupportTicket = z.object({
  category: z.enum(["billing", "technical", "account", "other"]),
  priority: z.enum(["low", "medium", "high"]),
  summary: z.string(),
});

const response = await ollama.chat({
  model: "gemma3",
  messages: [
    {
      role: "user",
      content: "I was charged twice this month and need a refund as soon as possible.",
    },
  ],
  format: zodToJsonSchema(SupportTicket),
  options: { temperature: 0 },
});

console.log(SupportTicket.parse(JSON.parse(response.message.content)));
