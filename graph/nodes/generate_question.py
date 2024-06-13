# generate.py
from typing import Any, Dict

from graph.chains.generate_question import generate_question_chain
from graph.state import GraphState
from graph.graph_utils import draw

def generate_question(state: GraphState) -> Dict[str, Any]:
    print("###GENERATE Questions###")
    question = state["question"]
    chat_history = state.get("chat_history", [])  # Get chat history from state, default to empty list
    draw("generate_question", state["theGraph"])
    print(chat_history)
    # Pass the chat history to the generation chain
    generated_question = generate_question_chain.invoke({"question": question, "chat_history": chat_history})
    # Update the state with the updated chat history
    print(generated_question)
    return {"question": generated_question}
