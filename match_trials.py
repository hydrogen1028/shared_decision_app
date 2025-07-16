import pandas as pd

def match_trials(patient_data, trial_file="data/clinical_trials.csv"):
    trials = pd.read_csv(trial_file)
    matches = trials[
        (trials["cancer_type"] == patient_data["cancer_type"]) &
        (trials["stage"] == patient_data["stage"]) &
        (trials["ECOG_min"] <= patient_data["ECOG"]) &
        (trials["ECOG_max"] >= patient_data["ECOG"])
    ]
    return matches
