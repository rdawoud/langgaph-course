#graph.py
from dotenv import load_dotenv
from langgraph.graph import END, StateGraph
from graph.consts import START,ROUTE_QUESTION, GENERATE, GRADE_DOCUMENTS, RETRIEVE, WEBSEARCH
from graph.nodes import start, generate,generate_question, grade_documents, retrieven4j,  web_search, process_input,decide_to_generate,check_hallucinations 
from graph.state import GraphState
from graph.graph_utils import draw

load_dotenv()

def route_node(state: GraphState):
    print("==Go To==> "+ state["thenode"] )
    return state["thenode"]

workflow = StateGraph(GraphState)
workflow.add_node(START, lambda state: start(state, workflow))
workflow.add_node("process_input",process_input)
workflow.add_node("retrieven4j", retrieven4j)
workflow.add_node(GRADE_DOCUMENTS, grade_documents)
workflow.add_node("decide_to_generate", decide_to_generate)
workflow.add_node(GENERATE, generate)
workflow.add_node("generate_question", generate_question)
workflow.add_node(WEBSEARCH, web_search)
#workflow.add_node("check_hallucinations",check_hallucinations)

workflow.set_entry_point(START)
workflow.add_edge(START,"process_input")
workflow.add_conditional_edges("process_input",
    route_node,
    {
        "generate_question": "generate_question",
        "vectorstore": "retrieven4j",
    },
)
workflow.add_edge("generate_question", WEBSEARCH)
workflow.add_edge("retrieven4j", GRADE_DOCUMENTS)
workflow.add_edge(GRADE_DOCUMENTS,"decide_to_generate")
workflow.add_conditional_edges(
    "decide_to_generate",
    route_node,
    {
        "generate_question": "generate_question",
        GENERATE: GENERATE,
    },
)
workflow.add_edge(WEBSEARCH, GENERATE)
workflow.add_edge(GENERATE, END)
#workflow.add_conditional_edges(
#    "check_hallucinations",
#    route_node,
#    {
#        "not supported": GENERATE,
#        "useful": END,
#        "not useful": WEBSEARCH,
#    },
#)

app = workflow.compile()
