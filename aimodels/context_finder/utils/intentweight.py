INTENT_WEIGHTS = {

    # Very dangerous
    "otp_request": 0.30,
    "password_request": 0.30,
    "pin_request": 0.30,

    # Financial information
    "card_details_request": 0.25,
    "bank_details_request": 0.25,
    "payment_request": 0.25,

    # Other strong indicators
    "suspicious_link": 0.15,
    "remote_access": 0.20,

    # Supporting signals
    "urgency": 0.10,
    "impersonation": 0.15,
}
