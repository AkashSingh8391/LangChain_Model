from langchain_ollama import ChatOllama

# TinyLlama model load
model = ChatOllama(
    model="tinyllama"
)

# Prompt
result = model.invoke("What is the capital of india")

# Output
print(result.content)