from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate

from graph.integrations.llm import llm

from langchain.prompts import PromptTemplate

template = """
You are an AI assistant that helps users find information on the web by adjusting their questions based on the conversation history.

Conversation History:
{chat_history}

Original Question: {question}

Using the provided conversation history, reformulate the original question to include any relevant context that would help in searching the web for the most appropriate information to answer the question. If the original question cannot be improved based on the conversation history, simply repeat the original question.

Reformulated Question:
"""

prompt = PromptTemplate(
    input_variables=["history", "question"], 
    template=template
)

generate_question_chain = prompt | llm | StrOutputParser()
