def detect_cross_chain(transactions):

    chains_detected = set()

    for tx in transactions:

        chain = tx.get("chain")

        if chain:
            chains_detected.add(chain)

    if len(chains_detected) > 1:

        return {
            "cross_chain": True,
            "chains": list(chains_detected)
        }

    else:

        return {
            "cross_chain": False,
            "chains": list(chains_detected)
        }