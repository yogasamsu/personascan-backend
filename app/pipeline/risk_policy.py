def determine_risk(scores: dict) -> str:
    if scores["hate_speech_score"] > 0.4:
        return "HIGH"
    if scores["toxicity_score"] > 0.3:
        return "MEDIUM"
    return "LOW"
