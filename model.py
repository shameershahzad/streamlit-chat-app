from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage

llm = ChatOllama(model="llama3.2")

def get_response(user,memory):
    memory.append(HumanMessage(content=user))

    response = llm.invoke(memory)
    memory.append(AIMessage(content=response.content))
    return response.content,memory
