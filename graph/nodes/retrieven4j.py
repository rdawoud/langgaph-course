from typing import Any, Dict

from graph.state import GraphState
from graph.chains.vector import vector

from graph.graph_utils import draw

def retrieven4j(state: GraphState) -> Dict[str, Any]:
    print("###RETRIEVE###")
    draw("retrieven4j", state["theGraph"])
    question = state["question"]

    documents = vector(question)
    print("===Retrived Docs ===")
    print(documents)
    return {"documents": documents, "question": question}
