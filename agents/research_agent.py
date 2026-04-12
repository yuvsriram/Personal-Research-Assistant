from llm.planner import create_plan
from tools.search_tool import search
from llm.summarizer import summarize
from memory.memory_store import memory

def run_research_agent(topic):
    questions = create_plan(topic)

    findings = []

    for q in questions:
        answer = search(q)
        memory.append({"q": q, "a": answer})
        findings.append(answer)

    final = summarize(topic, findings)
    return final