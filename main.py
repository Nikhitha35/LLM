from fastapi import FastAPI, Request
from scripts.parse_query import parse_user_query
from scripts.semantic_search import search_policy_clauses
from scripts.decision_engine import generate_decision

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "LLM Query API is running!"}

@app.post("/query")
async def process_query(request: Request):
    data = await request.json()
    query = data.get("query")

    if not query:
        return {"error": "Query not provided"}

    structured = parse_user_query(query)
    matched_clauses = search_policy_clauses(structured)
    decision = generate_decision(structured, matched_clauses)

    return {"response": decision}
