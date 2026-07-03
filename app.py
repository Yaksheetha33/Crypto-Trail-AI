from modules.tracer import trace_wallets
from modules.graph_builder import visualize_money_flow
from modules.mixer_detector import detect_mixer
from modules.cross_chain_tracker import detect_cross_chain
from modules.risk_engine import RiskEngine
from modules.cashout_detector import detect_cashout
from modules.kyc_info import get_exchange_kyc


# ----- DARKNET CHECK FUNCTION -----

def check_darknet(wallet_address):
    """
    Demo darknet check for Ethereum wallets
    """

    print(f"Checking darknet database for: {wallet_address}")

    # Demo suspicious rule
    if wallet_address.lower().startswith("0xce"):
        print(" Suspicious wallet detected (possible darknet link)")
        print("Source: Simulated blockchain intelligence database\n")
        return True

    else:
        print(" Wallet not found in darknet database\n")
        return False


# ----- MAIN FUNCTION -----

def main():

    print("==== Crypto Trail AI ====\n")

    yakshitha_wallet = input("Enter Yakshitha wallet address: ").lower()

    print("\nTracing wallet...\n")

    self_wallets, final_wallets = trace_wallets(yakshitha_wallet)

    # ----- PREPARE TRANSACTIONS -----

    transactions = []

    for w in self_wallets:
        transactions.append({
            "sender": yakshitha_wallet,
            "receiver": w,
            "chain": "ETH"
        })

    for w in final_wallets:
        transactions.append({
            "sender": "mediator_wallet",
            "receiver": w,
            "chain": "ETH"
        })

    # ----- MIXER DETECTION -----

    print("\n===== MIXER DETECTION =====\n")

    mixer_result = detect_mixer(transactions)

    if mixer_result["mixer_detected"]:
        print(" Mixers detected:")
        for m in mixer_result["mixer_wallets"]:
            print(m)
    else:
        print("No mixers detected")

    # ----- CROSS CHAIN DETECTION -----

    print("\n===== CROSS CHAIN DETECTION =====\n")

    cross_chain_result = detect_cross_chain(transactions)

    if cross_chain_result["cross_chain"]:
        print(" Cross-chain activity detected across:")
        for c in cross_chain_result["chains"]:
            print(c)
    else:
        print("No cross-chain activity detected")

    # ----- MEDIATOR WALLETS -----

    print("\n===== Mediator (Self) Wallets Detected =====\n")

    if self_wallets:
        for w in set(self_wallets):
            print(w)
    else:
        print("No mediator wallets detected")

    # ----- FINAL RECEIVER -----

    final_receiver = None

    print("\n===== Final Receiver (Possible Anushka) =====\n")

    if final_wallets:
        final_receiver = list(set(final_wallets))[0]
        print(final_receiver)
    else:
        print("No final wallet found")

    # ----- DARKNET CHECK -----

    print("\n===== DARKNET CHECK =====\n")

    darknet_flag = check_darknet(yakshitha_wallet)

    if final_receiver:
        check_darknet(final_receiver)

    # ----- CASHOUT DETECTION -----

    print("\n===== CASH OUT DETECTION =====\n")

    cashout_results = detect_cashout(transactions)

    if cashout_results:

        print(" Possible Crypto → Fiat Cashout Detected\n")

        for event in cashout_results:

            print("Exchange:", event["exchange"])
            print("Exchange Wallet:", event["wallet"])

            kyc = get_exchange_kyc(event["exchange"])

            if kyc:

                print("\nKYC Required:")

                for doc in kyc["documents"]:
                    print("-", doc)

                print("\nWithdrawal Methods:")

                for method in kyc["withdraw_methods"]:
                    print("-", method)

            print("\n----------------------------\n")

    else:
        print("No exchange cashout detected\n")

    # ----- RISK SCORE ENGINE -----

    print("\n===== RISK ANALYSIS =====\n")

    risk_engine = RiskEngine()

    outgoing_wallets = list(set(self_wallets))

    # simulate transaction values
    risk_transactions = []

    for w in outgoing_wallets:
        risk_transactions.append({
            "to": w,
            "value": 12
        })

    mixer_flag = mixer_result["mixer_detected"]
    cashout_flag = len(cashout_results) > 0

    score, reasons = risk_engine.calculate_risk(
        risk_transactions,
        outgoing_wallets,
        mixer_detected=mixer_flag,
        darknet=darknet_flag,
        cashout=cashout_flag
    )

    level = risk_engine.risk_level(score)

    print("Risk Score:", score)
    print("Risk Level:", level)

    print("\nReasons:")
    for r in reasons:
        print("-", r)

    # ----- GRAPH VISUALIZATION -----

    visualize_money_flow(
        yakshitha_wallet,
        list(set(self_wallets)),
        final_receiver
    )


# ----- RUN PROGRAM -----

if __name__ == "__main__":
    main()