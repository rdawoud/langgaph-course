# generate.py
from typing import Any, Dict

from graph.chains.generation import generation_chain
from graph.state import GraphState
from graph.graph_utils import draw

def generate(state: GraphState) -> Dict[str, Any]:
    print("###GENERATE###")
    question = state["question"]
    documents = state["documents"]
    chat_history = state.get("chat_history", [])  # Get chat history from state, default to empty list
    draw("generate", state["theGraph"])
    # Pass the chat history to the generation chain
    generation = generation_chain.invoke({"context": documents, "question": question, "chat_history": chat_history})
    # Update the state with the updated chat history
    print("=========")
    print(question)
    print("=========")
    print(*chat_history, sep='\n')
    print("=========")
    print(generation )
    print("=========")
    return {"documents": documents, "question": question, "generation": generation}
