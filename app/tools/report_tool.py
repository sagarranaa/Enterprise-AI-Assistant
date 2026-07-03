import json


def report_tool():

    with open("app/data/tickets.json") as f:
        tickets = json.load(f)

    total = len(tickets)

    return f"""
Monthly Report

Total Tickets : {total}

Status : Generated Successfully
"""