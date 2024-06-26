from typing import Any, Dict
from graph.state import GraphState
from graph.graph_utils import draw

from graph.consts import START,ROUTE_QUESTION, GENERATE, GRADE_DOCUMENTS, RETRIEVE, WEBSEARCH

from graph.chains.hallucination_grader import hallucination_grader
from graph.chains.answer_grader import answer_grader

def check_hallucinations(state: GraphState) -> Dict[str, Any]:
    print("###CHECK HALLUCINATIONS###")
    draw("check_hallucinations", state["theGraph"])
    question = state["question"]
    documents = state["documents"]
    generation = state["generation"]
    history = state["chat_history"]
    score = hallucination_grader.invoke(
        {"documents": documents, "generation": generation}
    )
    print("====question=====")
    print(question)
    print("====Documents=====")
    print(*documents, sep='\n' )
    print("====genration=====")
    print(generation)
    if hallucination_grade := score.binary_score:
        print("---DECISION: GENERATION IS GROUNDED IN DOCUMENTS---")
        print("---GRADE GENERATION vs QUESTION---")
        score = answer_grader.invoke({"question": question, "generation": generation})
        if answer_grade := score.binary_score:
            print("---DECISION: GENERATION ADDRESSES QUESTION---")
            return ({"thenode": "useful","question": question, "generation": generation})
        else:
            print("---DECISION: GENERATION DOES NOT ADDRESS QUESTION---")
            history.append({"role": "user", "content": question})
            history.append({"role": "system", "content": generation})
            history.append({"role": "user", "content": "answer is not correct"})
            return ({"thenode": "not useful","question": question, "generation": generation, "chat_history": history})
    else:
        print("---DECISION: GENERATION IS NOT GROUNDED IN DOCUMENTS, RE-TRY---")
        return ({"thenode": "not supported","question": question, "generation": generation})
