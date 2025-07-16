import json

def get_matched_therapies(patient_data):
    with open("data/cancer_guidelines.json", "r") as f:
        guidelines = json.load(f)

    cancer_info = guidelines.get(patient_data["cancer_type"], {})
    stage_info = cancer_info.get(patient_data["stage"], [])

    matched = []
    for therapy in stage_info:
        elig = therapy["eligibility"]
        if patient_data["ECOG"] in elig["ECOG"] and elig["age"][0] <= patient_data["age"] <= elig["age"][1]:
            matched.append(therapy)
    return matched
