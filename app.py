from llm.planner import create_research_plan
from tools.search_tool import search_web
from llm.summarizer import summarize_research
import mlflow

if __name__ == "__main__":
    topic = input("Enter topic: ")


    questions = create_research_plan(topic)

    findings = []

    for q in questions:
        result = search_web(q)
        findings.append(result)

    final_report = summarize_research(topic, findings)

    print(final_report)