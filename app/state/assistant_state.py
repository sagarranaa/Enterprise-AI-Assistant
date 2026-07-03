from typing import TypedDict


class AssistantState(TypedDict):
    question: str
    intent: str
    response: str