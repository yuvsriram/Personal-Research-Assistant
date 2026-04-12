from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(temperature=0.3)

def summarize_research(topic, findings):
    combined = "\n".join(findings)

    prompt = f"""
    You are a senior research analyst.

    Topic: {topic}

    Based on the research data below, generate a structured report.

    Format:
    1. Key Insights
    2. Benefits
    3. Challenges
    4. Future Outlook

    Keep it concise and clear.
    Avoid repeating information.

    Research Data:
    {combined}
    """

    response = llm.invoke([
        HumanMessage(content=prompt)
    ])

    return response.content