from langchain_groq import ChatGroq
import ENVConstants

def get_llm(model_name="llama-3.3-70b-versatile", temperature=0.2):
    llm = ChatGroq(model=model_name, temperature=temperature, api_key=ENVConstants.GROQ_API_KEY)
    return llm