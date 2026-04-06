from langchain_ollama import OllamaLLM
def get_llm(model='gemma3n:latest', temperature=0.2):
    llm = OllamaLLM(model=model, temperature=temperature)
    return llm
