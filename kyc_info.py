def get_exchange_kyc(exchange_name):

    exchanges = {

        "Binance": {
            "kyc_required": True,
            "documents": [
                "Government ID",
                "Passport / Driving License",
                "Selfie Verification",
                "Address Proof",
                "Phone Number",
                "Email Verification"
            ],
            "withdraw_methods": [
                "Bank Transfer",
                "Debit Card",
                "P2P Trading",
                "UPI (India)"
            ]
        },

        "Unknown Exchange": {
            "kyc_required": True,
            "documents": [
                "Government ID",
                "Face Verification",
                "Phone Number"
            ],
            "withdraw_methods": [
                "Bank Transfer",
                "Crypto Withdrawal"
            ]
        }

    }

    return exchanges.get(exchange_name, {})