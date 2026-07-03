import networkx as nx
import matplotlib.pyplot as plt


def visualize_money_flow(sender_wallet, mediator_wallets, final_receiver):

    G = nx.DiGraph()

    # add sender
    G.add_node(sender_wallet)

    # add mediators
    for wallet in mediator_wallets:
        G.add_node(wallet)
        G.add_edge(sender_wallet, wallet)

    # add final receiver
    if final_receiver:
        G.add_node(final_receiver)

        for wallet in mediator_wallets:
            G.add_edge(wallet, final_receiver)

    # node colors
    colors = []

    for node in G.nodes():

        if node == sender_wallet:
            colors.append("green")

        elif node == final_receiver:
            colors.append("red")

        else:
            colors.append("blue")

    pos = nx.spring_layout(G)

    plt.figure(figsize=(10,7))

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color=colors,
        node_size=2500,
        font_size=8,
        arrows=True
    )

    plt.title("Crypto Money Flow Graph")

    plt.show()