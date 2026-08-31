from aimodels.context_finder.utils.intentweight import INTENT_WEIGHTS

def calculate_risk(
    scam_probability: float,
    intents: dict
):
    """
    Combines ML scam probability with explicit suspicious intents.

    Important:
    The result is an MVP risk score, NOT a calibrated probability.
    """

    risk = scam_probability

    # Add rule-based evidence.
    for intent, detected in intents.items():

        if detected:
            risk += INTENT_WEIGHTS.get(intent, 0.0)

    # Cap at 1.0
    risk = min(risk, 1.0)

    return risk

