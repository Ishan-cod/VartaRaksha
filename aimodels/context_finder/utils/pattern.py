PATTERNS = {

    # --------------------------------------------------------
    # OTP / verification code
    # --------------------------------------------------------

    "otp_request": [
        r"\botp\b",
        r"one[\s-]*time[\s-]*(password|passcode|code)",
        r"verification[\s-]*code",
        r"security[\s-]*code",
        r"authentication[\s-]*code",

        r"(tell|give|share|read|provide|send).{0,40}"
        r"(otp|code|passcode)",

        r"(otp|code|passcode).{0,40}"
        r"(tell|give|share|read|provide|send)",
    ],


    # --------------------------------------------------------
    # Password
    # --------------------------------------------------------

    "password_request": [
        r"(tell|give|share|send|provide).{0,40}"
        r"(your|the)?\s*password",

        r"(password).{0,40}"
        r"(tell|give|share|send|provide)",

        r"login[\s-]*password",
        r"account[\s-]*password",
    ],


    # --------------------------------------------------------
    # PIN / UPI PIN
    # --------------------------------------------------------

    "pin_request": [
        r"\bupi[\s-]*pin\b",
        r"\batm[\s-]*pin\b",
        r"\bcard[\s-]*pin\b",
        r"\bpin\b.{0,30}"
        r"(tell|give|share|send|provide)",

        r"(tell|give|share|send|provide).{0,30}"
        r"\bpin\b",
    ],


    # --------------------------------------------------------
    # Card details
    # --------------------------------------------------------

    "card_details_request": [
        r"\bcard[\s-]*number\b",
        r"\bcredit[\s-]*card\b",
        r"\bdebit[\s-]*card\b",
        r"\bcvv\b",
        r"\bcvc\b",
        r"expiry[\s-]*(date|month)",
        r"expiration[\s-]*(date|month)",

        r"(tell|give|share|send|provide).{0,40}"
        r"(card number|cvv|cvc)",
    ],


    # --------------------------------------------------------
    # Bank information
    # --------------------------------------------------------

    "bank_details_request": [
        r"\bbank[\s-]*account\b",
        r"\baccount[\s-]*number\b",
        r"\bifsc\b",
        r"\bbank[\s-]*details\b",

        r"(tell|give|share|send|provide).{0,40}"
        r"(account number|ifsc|bank details)",
    ],


    # --------------------------------------------------------
    # Money / payment
    # --------------------------------------------------------

    "payment_request": [
        r"send.{0,50}(money|cash|rupees|rs\.?|₹)",
        r"transfer.{0,50}(money|cash|rupees|rs\.?|₹)",
        r"pay.{0,50}(money|cash|rupees|rs\.?|₹)",
        r"make.{0,30}(payment|transfer)",
        r"payment.{0,40}(now|immediately|today)",
        r"transfer.{0,40}(now|immediately|today)",

        r"\bupi\b.{0,50}"
        r"(pay|payment|transfer|send)",

        r"(send|transfer|pay).{0,50}"
        r"(amount|₹|rupees|rs\b)",
    ],


    # --------------------------------------------------------
    # Suspicious links / phishing
    # --------------------------------------------------------

    "suspicious_link": [
        r"https?://",
        r"www\.",
        r"click.{0,30}(link|here)",
        r"open.{0,30}(link|website)",
        r"visit.{0,30}(link|website)",
        r"log.?in.{0,30}(link|website)",
    ],


    # --------------------------------------------------------
    # Remote access
    # --------------------------------------------------------

    "remote_access": [
        r"\banydesk\b",
        r"\bteamviewer\b",
        r"\brustdesk\b",
        r"remote[\s-]*access",
        r"remote[\s-]*control",
        r"screen[\s-]*sharing",
        r"share[\s-]+your[\s-]+screen",
        r"install.{0,50}(app|application|software)",
    ],


    # --------------------------------------------------------
    # Urgency / pressure
    # --------------------------------------------------------

    "urgency": [
        r"\bimmediately\b",
        r"\bright now\b",
        r"\burgent\b",
        r"\basap\b",

        r"account.{0,50}"
        r"(blocked|suspended|closed|terminated)",

        r"within.{0,30}"
        r"(minute|minutes|hour|hours)",

        r"last[\s-]*warning",
        r"final[\s-]*warning",
    ],


    # --------------------------------------------------------
    # Impersonation
    # --------------------------------------------------------

    "impersonation": [
        r"calling from.{0,50}"
        r"(bank|police|government|income tax|rbi|support)",

        r"i am from.{0,50}"
        r"(bank|police|government|rbi|support)",

        r"customer[\s-]*care",
        r"bank official",
        r"government official",
        r"police officer",
        r"cyber crime",
        r"rbi officer",
    ],
}