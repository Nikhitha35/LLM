def generate_decision(query_structured, policy_clauses):
    decision = {
        "decision": "Rejected",
        "amount": 0,
        "justification": "Procedure not found in policy",
        "clause_reference": None
    }

    for clause in policy_clauses:
        if query_structured["procedure"]:
            proc_words = query_structured["procedure"].lower().split()
            if all(word in clause.lower() for word in proc_words):
                decision["decision"] = "Approved"
                decision["amount"] = 50000
                decision["justification"] = f"{query_structured['procedure']} is covered as per policy."
                decision["clause_reference"] = clause[:150]
                break


    return decision
