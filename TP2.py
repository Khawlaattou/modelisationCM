import networkx as nx
import matplotlib.pyplot as plt

def m_transition(r):
    P = [[0 for _ in range(r)] for _ in range(r)]

    for i in range(r):
        for j in range(r):
            if j == i + 1 and i < r - 1:
                P[i][j] = ((r - i) ** 2) / (r ** 2)
            elif j == i - 1 and i > 0:
                P[i][j] = (i ** 2) / (r ** 2)
            elif j == i:
                P[i][j] = (2 * i * (r - i)) / (r ** 2)

    return P

r = int(input("Enter a number r: "))
transition_matrix = m_transition(r)
print(transition_matrix)
# Create directed graph representing the Markov chain
G = nx.DiGraph()
G.add_nodes_from(range(r))

# Adding multiple edges with different labels between nodes
for i in range(len(transition_matrix)):
    for j in range(len(transition_matrix[i])):
        if transition_matrix[i][j] != 0:  # Checking if the value is non-zero before adding the edge
            G.add_edge(i, j, weight=f"{transition_matrix[i][j]:.2f}")  # First edge with label
            G.add_edge(i, j, weight=f"{transition_matrix[i][j]:.2f}")  # Second edge with different label

# Drawing the graph with edge labels at the end of each edge
pos = nx.circular_layout(G)
edge_labels = {(i, j): d['weight'] for i, j, d in G.edges(data=True)}

# Separate edges based on labels for visualization
edges_label1 = [(u, v) for u, v, d in G.edges(data=True) if 'Label 1' in d['weight']]
edges_label2 = [(u, v) for u, v, d in G.edges(data=True) if 'Label 2' in d['weight']]

# Separate self-loop edges and their labels
self_loop_edges = [(u, v) for u, v in G.edges() if u == v]
self_loop_labels = {(i, i): d['weight'] for i, j, d in G.edges(data=True) if i == j}

nx.draw(G, pos, with_labels=True, node_size=300, node_color='purple', font_weight='bold', arrows=True)
nx.draw_networkx_edges(G, pos, edgelist=edges_label1, width=1.0, alpha=0.7,  arrows=True)
nx.draw_networkx_edges(G, pos, edgelist=edges_label2, width=1.0, alpha=0.7,  arrows=True)
nx.draw_networkx_edges(G, pos, edgelist=self_loop_edges, width=1.0, alpha=0.7, edge_color='purple', arrows=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.3, font_color='black', font_size=8)
nx.draw_networkx_edge_labels(G, pos, edge_labels=self_loop_labels, label_pos=-0.3, font_color='purple', font_size=8)

plt.title('CM basée sur la matrice de transition generé')
plt.show()

