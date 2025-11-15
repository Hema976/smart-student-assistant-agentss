qa = {
    "oop": "OOP = Encapsulation, Inheritance, Polymorphism, Abstraction.",
    "dbms": "DBMS = Database Management System.",
    "ai": "AI is the simulation of human intelligence by machines.",
    "datastructure": "DS includes arrays, stacks, queues, linked lists."
}

def answer_doubt(query):
    query = query.lower()
    for key in qa:
        if key in query:
            return qa[key]
    return "Sorry, I don't know this query yet."
