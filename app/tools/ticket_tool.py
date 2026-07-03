import json
from datetime import datetime


def ticket_tool(question: str):

    with open("app/data/tickets.json") as f:
        tickets = json.load(f)

    ticket = {
        "id": len(tickets)+1,
        "issue": question,
        "status": "Open",
        "created_at": str(datetime.now())
    }

    tickets.append(ticket)

    with open("app/data/tickets.json","w") as f:
        json.dump(tickets,f,indent=4)

    return f"Ticket Created Successfully.\nTicket ID : {ticket['id']}"