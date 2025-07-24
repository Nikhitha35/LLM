import re

def parse_user_query(query):
    query = query.lower()

    # Extract age
    age_match = re.search(r'(\d+)[ -]?year[- ]?old', query)
    age = int(age_match.group(1)) if age_match else None

    # Extract gender
    gender = None
    if "male" in query or "m" in query:
        gender = "male"
    elif "female" in query or "f" in query:
        gender = "female"

    # Extract procedure (simple list)
    procedure = {
    "knee surgery": ["knee operation", "joint replacement", "orthopedic procedure"],
    "angioplasty": ["heart ballooning", "artery clearing"],
    # add more
}
    procedure = next((p for p in procedure if p in query), None)

    # Extract location
    location_match = re.search(r'in ([a-zA-Z ]+)', query)
    location = location_match.group(1).strip() if location_match else None

    # Extract policy duration
    duration_match = re.search(r'(\d+)[ -]?(month|months|mo)[- ]?(old|policy)?', query)
    policy_duration_months = int(duration_match.group(1)) if duration_match else None

    return {
        "age": age,
        "gender": gender,
        "procedure": procedure,
        "location": location,
        "policy_duration_months": policy_duration_months
    }
