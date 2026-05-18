import ollama from "ollama";
import { z } from "zod";
import { zodToJsonSchema } from "zod-to-json-schema";

const Pet = z.object({
  name: z.string(),
  animal: z.string(),
  age: z.number(),
});

const PetList = z.object({
  pets: z.array(Pet),
});

const response = await ollama.chat({
  model: "gemma3",
  messages: [
    {
      role: "user",
      content: "I have a 3-year-old dog named Bori and a 2-year-old cat named Nabi.",
    },
  ],
  format: zodToJsonSchema(PetList),
  options: { temperature: 0 },
});

console.log(PetList.parse(JSON.parse(response.message.content)));
