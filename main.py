from openai import OpenAI
import os
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENROUTER_API_KEY"),
)
print(client.api_key)
completion = client.chat.completions.create(
  extra_body={},
  model="deepseek/deepseek-r1-0528-qwen3-8b:free",
  messages=[
    {
      "role": "user",
      "content": "What is the meaning of life?"
    }
  ]
)
print(completion.choices[0].message.content)