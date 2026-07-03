import requests

API_URL = "https://www.bitcoinabuse.com/api/reports/check"
API_KEY = "YOUR_API_KEY_HERE"

SOURCE_NAME = "Bitcoin Abuse Database"
SOURCE_URL = "https://www.bitcoinabuse.com"


def check_darknet_wallet(wallet):

    params = {
        "address": wallet,
        "api_token": API_KEY
    }

    try:
        response = requests.get(API_URL, params=params)

        # check if response is valid
        if response.status_code != 200:
            print("API connection failed. Status:", response.status_code)
            return False, 0, SOURCE_NAME, SOURCE_URL

        try:
            data = response.json()
        except:
            print("Invalid response from darknet database")
            return False, 0, SOURCE_NAME, SOURCE_URL

        count = data.get("count", 0)

        if count > 0:
            return True, count, SOURCE_NAME, SOURCE_URL
        else:
            return False, 0, SOURCE_NAME, SOURCE_URL

    except Exception as e:
        print("Error connecting to darknet database:", e)
        return False, 0, SOURCE_NAME, SOURCE_URL
    # darknet_checker.py
SUSPICIOUS_WALLETS = [
    "0xceb239e2b3410b270779d4c2d07f956700f08304",
    "0x1234567890abcdef1234567890abcdef12345678"
]

SOURCE_NAME = "Internal Darknet Intelligence DB"
SOURCE_URL = "Local Investigation Database"


def check_darknet_wallet(wallet):

    wallet = wallet.lower()

    if wallet in SUSPICIOUS_WALLETS:
        return True, 1, SOURCE_NAME, SOURCE_URL
    else:
        return False, 0, SOURCE_NAME, SOURCE_URL