import json
import os


def load_mixers():
    # Get project root folder
    base_dir = os.path.dirname(os.path.dirname(__file__))

    # Build correct path to JSON file
    file_path = os.path.join(base_dir, "database", "mixer_wallets.json")

    with open(file_path, "r") as f:
        data = json.load(f)

    return data["mixers"]


def detect_mixer(transactions):

    mixers = load_mixers()

    mixer_found = False
    mixer_wallets = []

    for tx in transactions:
        receiver = tx["receiver"]

        if receiver in mixers:
            mixer_found = True
            mixer_wallets.append(receiver)

    return {
        "mixer_detected": mixer_found,
        "mixer_wallets": list(set(mixer_wallets))
    }