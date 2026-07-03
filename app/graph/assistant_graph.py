from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage

from app.llm.client import get_llm
from app.prompts.system_prompt import SYSTEM_PROMPT
from app.state.assistant_state import AssistantState

from app.tools.employee_tool import employee_tool
from app.tools.ticket_tool import ticket_tool
from app.tools.report_tool import report_tool

llm = get_llm()


def assistant_node(state: AssistantState):
    """
    Main Assistant Node
    """

    question = state["question"]

    print("\n🤖 Enterprise Assistant Started...")
    print(f"Question: {question}")

    response = llm.invoke(
        [
            HumanMessage(
                content=f"{SYSTEM_PROMPT}\n\nUser Question:\n{question}"
            )
        ]
    )

    intent = response.content.strip().lower()

    print(f"Detected Intent : {intent}")

    state["intent"] = intent

    if intent == "employee":
        state["response"] = employee_tool(question)

    elif intent == "ticket":
        state["response"] = ticket_tool(question)

    elif intent == "report":
        state["response"] = report_tool()

    else:
        answer = llm.invoke(question)
        state["response"] = answer.content

    return state


# -------------------------------
# LangGraph Workflow
# -------------------------------

workflow = StateGraph(AssistantState)

workflow.add_node("assistant", assistant_node)

workflow.set_entry_point("assistant")

workflow.add_edge("assistant", END)

graph = workflow.compile()