from ollama import Client

client = Client()

response = client.chat(
    model="phi3",
    messages=[
        {"role": "user", "content": "Explain warehouse automation in one paragraph"}
    ],
)

print(response["message"]["content"])