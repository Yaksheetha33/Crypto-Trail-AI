from modules.fetch_transactions import fetch_transactions


def trace_wallets(yakshitha_wallet):

    transactions = fetch_transactions(yakshitha_wallet)

    if not transactions:
        return [], []

    self_wallets = []
    final_receivers = []

    for tx in transactions:

        if tx["sender"].lower() == yakshitha_wallet.lower():

            receiver = tx["receiver"]
            self_wallets.append(receiver)

            receiver_txs = fetch_transactions(receiver)

            for rtx in receiver_txs:

                if rtx["sender"].lower() == receiver.lower():

                    final_receivers.append(rtx["receiver"])

    return self_wallets, final_receivers