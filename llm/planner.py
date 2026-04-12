import re
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(temperature=0.3)

def create_research_plan(topic):
    prompt = f"""
    Break the following topic into 3 to 5 clear research questions.

    Topic: {topic}

    Return only questions as a list.
    """

    response = llm.invoke([
        HumanMessage(content=prompt)
    ])

    lines = response.content.split("\n")

    clean_questions = []
    for line in lines:
        # 🔥 THIS is the key fix
        line = re.sub(r"^\d+\.\s*", "", line)  # removes "1. ", "2. "
        line = line.strip("- ").strip()
        
        if line:
            clean_questions.append(line)

    return clean_questions