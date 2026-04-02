from langchain.memory import ConversationBufferMemory

# -----------------------------
# AGENT MEMORY
# -----------------------------

research_memory = ConversationBufferMemory()
summary_memory = ConversationBufferMemory()

# Shared memory between agents
shared_memory = []


# -----------------------------
# RESEARCH AGENT
# -----------------------------

def research_agent(topic):

    research_data = {
        "artificial intelligence":
        "Artificial Intelligence (AI) is a field of computer science that focuses on creating machines that can perform tasks requiring human intelligence such as learning, reasoning, and problem solving.",

        "machine learning":
        "Machine Learning is a subset of AI that allows computers to learn patterns from data and make predictions without being explicitly programmed.",

        "python":
        "Python is a high level programming language widely used in AI, data science, automation, and web development."
    }

    topic = topic.lower()

    if topic in research_data:
        result = research_data[topic]
    else:
        result = f"I found general information about {topic}. It is an interesting topic in technology and science."

    # Store in research agent memory
    research_memory.save_context(
        {"input": topic},
        {"output": result}
    )

    # Store in shared memory
    shared_memory.append(result)

    return result


# -----------------------------
# SUMMARIZER AGENT
# -----------------------------

def summarizer_agent(text):

    words = text.split()

    # Simple summarization
    summary = " ".join(words[:20]) + "..."

    # Store in summarizer memory
    summary_memory.save_context(
        {"input": text},
        {"output": summary}
    )

    return summary


# -----------------------------
# ORCHESTRATION LOGIC
# -----------------------------

def multi_agent_system(user_query):

    print("\nResearch Agent working...\n")

    research_result = research_agent(user_query)

    print("Research Result:")
    print(research_result)

    print("\nSending research to Summarizer Agent...\n")

    summary = summarizer_agent(research_result)

    print("Summary:")
    print(summary)

    return summary


# -----------------------------
# CONSOLE INTERFACE
# -----------------------------

print("=== Multi-Agent System with Memory ===")
print("Agents: Research Agent + Summarizer Agent")
print("Type 'memory' to view shared memory")
print("Type 'exit' to quit\n")


while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    if user_input.lower() == "memory":
        print("\nShared Memory:")
        for item in shared_memory:
            print("-", item)
        print()
        continue

    multi_agent_system(user_input)