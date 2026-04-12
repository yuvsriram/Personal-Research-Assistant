from langchain_community.tools import DuckDuckGoSearchRun

search = DuckDuckGoSearchRun()

def search_web(query):
    result = search.run(query)
    return result