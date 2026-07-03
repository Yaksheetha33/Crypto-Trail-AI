
import requests
from datetime import datetime

API_KEY = "E6UH842VRZFFATNZMBVUFPUGK6CHUAR5QR"

def fetch_transactions(wallet):

    url = (
        "https://api.etherscan.io/v2/api"
        "?chainid=11155111"
        "&module=account"
        "&action=txlist"
        f"&address={wallet}"
        "&startblock=0"
        "&endblock=99999999"
        "&sort=asc"
        f"&apikey={API_KEY}"
    )

    response = requests.get(url)
    data = response.json()

    print("\nFULL API RESPONSE:")
    print(data)

    if data["status"] != "1":
        print("No transactions returned from API")
        return []

    transactions = []

    for tx in data["result"]:

        sender = tx["from"]
        receiver = tx["to"]

        value_eth = int(tx["value"]) / 10**18

        timestamp = datetime.fromtimestamp(
            int(tx["timeStamp"])
        ).strftime("%Y-%m-%d %H:%M:%S")

        transactions.append({
            "sender": sender.lower(),
            "receiver": receiver.lower(),
            "amount": value_eth,
            "timestamp": timestamp
        })

    print("Transactions fetched:", len(transactions))

    return transactions