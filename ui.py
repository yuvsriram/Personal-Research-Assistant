import streamlit as st
from llm.planner import create_research_plan
from tools.search_tool import search_web
from llm.summarizer import summarize_research

st.title("Personal Research Assistant")

topic = st.text_input("Enter a topic:")

if st.button("Research"):
    if topic:
        st.write("🔍 Researching...")

        questions = create_research_plan(topic)

        findings = []

        for q in questions:
            st.write(f"➡️ {q}")
            result = search_web(q)
            findings.append(result)

        st.write("Generating report...")

        final_report = summarize_research(topic, findings)

        st.subheader("Final Report")
        st.write(final_report)
    else:
        st.warning("Please enter a topic")
