from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.graph.assistant_graph import graph

router = APIRouter()


class AskRequest(BaseModel):
    question: str


@router.post("/ask")
def ask(request: AskRequest):
    try:
        state = {
            "question": request.question,
            "intent": "",
            "response": ""
        }

        result = graph.invoke(state)

        return {
            "response": result["response"]
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )