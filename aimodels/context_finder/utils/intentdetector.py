import re
from aimodels.context_finder.utils.pattern import PATTERNS

def detect_intents(text: str):
    """
    Detects explicit suspicious intents using regex rules.

    Returns:
        {
            "otp_request": True,
            "password_request": False,
            ...
        }
    """

    text = text.lower()

    detected = {}

    for intent, patterns in PATTERNS.items():

        detected[intent] = False

        for pattern in patterns:

            if re.search(pattern, text):
                detected[intent] = True
                break

    return detected