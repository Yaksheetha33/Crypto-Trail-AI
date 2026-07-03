import requests

# -------- CHECK IF ADDRESS BELONGS TO EXCHANGE --------

def check_exchange_tag(address):
    """
    Detect if wallet belongs to an exchange using blockchain APIs
    """

    try:
        url = f"https://api.blockcypher.com/v1/eth/main/addrs/{address}"
        response = requests.get(url)

        if response.status_code != 200:
            return None

        data = response.json()

        # Example tag detection (demo logic)
        if "exchange" in str(data).lower():
            return "Unknown Exchange"

    except:
        pass

    return None


# -------- CASHOUT DETECTION --------

def detect_cashout(transactions):

    cashout_events = []

    for tx in transactions:

        receiver = tx.get("receiver")

        exchange = check_exchange_tag(receiver)

        if exchange:
            event = {
                "type": "CASH_OUT",
                "exchange": exchange,
                "wallet": receiver,
                "risk": "Funds moving to centralized exchange"
            }

            cashout_events.append(event)

    return cashout_events