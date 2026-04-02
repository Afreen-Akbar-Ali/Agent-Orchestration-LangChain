from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda

# Simulated intelligent LLM
def fake_llm(question: str) -> str:
    question = question.lower()

    if "hello" in question:
        return "Hello! How can I assist you today?"
    elif "ai" in question:
        return "Artificial Intelligence (AI) is the simulation of human intelligence by machines."
    elif "python" in question:
        return "Python is a popular programming language used for web development, AI, and data science."
    else:
        return f"I received your question: '{question}'. This is a simulated response."

# Wrap simulated model
llm = RunnableLambda(fake_llm)

print("=== LangChain Console Agent (Simulated LLM) ===")
print("Type 'exit' to quit\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    response = llm.invoke(user_input)

    print("AI:", response)
    print()