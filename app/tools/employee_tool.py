import json


def employee_tool(question: str):

    with open("app/data/employees.json") as f:
        employees = json.load(f)

    question = question.lower()

    for employee in employees:

        if employee["name"].lower().split()[0] in question:

            return (
                f"Employee Found\n\n"
                f"Name: {employee['name']}\n"
                f"Department: {employee['department']}\n"
                f"Email: {employee['email']}"
            )

    return "Employee not found."