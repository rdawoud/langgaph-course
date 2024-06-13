from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.runnables import RunnableSequence

from graph.integrations.llm import llm


class GradeHallucinations(BaseModel):
    """Binary score for hallucination present in generation answer."""

    binary_score: bool = Field(
        description="Answer is grounded in the facts, 'yes' or 'no'"
    )


structured_llm_grader = llm.with_structured_output(GradeHallucinations)

system = """You are a grader assessing whether an LLM generation is grounded in / supported by a set of retrieved facts.

Provide a binary score:
- 'yes' if the answer is fully grounded in / supported by the set of facts .
- 'no' if the answer contains information not found in the facts or if it contradicts the facts.

Examples:
- If the facts mention 'The sky is blue' and the generation says 'The sky is blue on a clear day', score it as 'yes'.
- If the facts do not mention the color of the sky and the generation says 'The sky is green', score it as 'no'.

Focus on assessing the factual accuracy and groundedness of the generation based on the given facts."""
hallucination_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "Set of facts: \n\n {documents} \n\n LLM generation: {generation}"),
    ]
)

hallucination_grader = hallucination_prompt | structured_llm_grader
