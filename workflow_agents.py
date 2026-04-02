from langchain.memory import ConversationBufferMemory

# -----------------------------
# MEMORY
# -----------------------------

research_memory = ConversationBufferMemory()
summary_memory = ConversationBufferMemory()
email_memory = ConversationBufferMemory()

shared_memory = []

# -----------------------------
# AGENT 1 — RESEARCH AGENT
# -----------------------------

def research_agent(topic):

    topic = topic.lower()

    data = {

        "artificial intelligence":
        "Artificial Intelligence is the simulation of human intelligence in machines that are programmed to think and learn.",

        "machine learning":
        "Machine learning is a subset of artificial intelligence that enables systems to learn from data and improve automatically.",

        "python":
        "Python is a popular programming language used for web development, data science, automation, and artificial intelligence.",

        "data science":
        "Data Science involves collecting, analyzing, and interpreting large amounts of data to extract useful insights."
    }

    result = data.get(
        topic,
        f"{topic} is an important concept in technology and innovation."
    )

    # store memory
    research_memory.save_context(
        {"input": topic},
        {"output": result}
    )

    shared_memory.append(result)

    return result


# -----------------------------
# AGENT 2 — SUMMARIZER AGENT
# -----------------------------

def summarizer_agent(text):

    summary_map = {

        "Artificial Intelligence is the simulation of human intelligence in machines that are programmed to think and learn.":
        "AI allows machines to think, learn, and perform intelligent tasks.",

        "Machine learning is a subset of artificial intelligence that enables systems to learn from data and improve automatically.":
        "Machine Learning helps computers learn patterns from data.",

        "Python is a popular programming language used for web development, data science, automation, and artificial intelligence.":
        "Python is widely used for AI, automation, and web development.",

        "Data Science involves collecting, analyzing, and interpreting large amounts of data to extract useful insights.":
        "Data Science helps extract insights from large datasets."
    }

    summary = summary_map.get(
        text,
        "This topic describes an important technical concept."
    )

    summary_memory.save_context(
        {"input": text},
        {"output": summary}
    )

    return summary


# -----------------------------
# AGENT 3 — EMAIL AGENT
# -----------------------------

def email_agent(summary):

    email = f"""
Subject: Information Summary

Hello,

Here is the requested information:

{summary}

Regards,
AI Assistant
"""

    email_memory.save_context(
        {"input": summary},
        {"output": email}
    )

    return email


# -----------------------------
# MAIN WORKFLOW FUNCTION
# -----------------------------

def run_workflow(topic):

    research = research_agent(topic)

    summary = summarizer_agent(research)

    email = email_agent(summary)

    return {

        "research": research,

        "summary": summary,

        "email": email

    }