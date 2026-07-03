class RiskEngine:

    def __init__(self):
        self.large_tx_threshold = 10
        self.max_outgoing_wallets = 4

    def calculate_risk(self, transactions, outgoing_wallets, mixer_detected=False, darknet=False, cashout=False):

        score = 0
        reasons = []

        # Large transaction detection
        for tx in transactions:
            if tx["value"] > self.large_tx_threshold:
                score += 25
                reasons.append("Large transaction detected")
                break

        # Splitting to many wallets
        if len(outgoing_wallets) > self.max_outgoing_wallets:
            score += 20
            reasons.append("Funds split to many wallets")

        # Mixer usage
        if mixer_detected:
            score += 30
            reasons.append("Mixer interaction detected")

        # Darknet interaction
        if darknet:
            score += 35
            reasons.append("Darknet wallet interaction")

        return score, reasons


    def risk_level(self, score):

        if score <= 30:
            return "LOW RISK"
        elif score <= 60:
            return "MEDIUM RISK"
        else:
            return "HIGH RISK"