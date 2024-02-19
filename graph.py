import networkx as nx
import matplotlib.pyplot as plt

# Load the dataset into a NetworkX graph
# Replace 'path/to/dataset' with the actual path to your dataset file
G = nx.read_edgelist('bio-CE-HT.edges')

# Print graph summarization
print("Graph summarization:")
print(nx.info(G))

# Degree distribution
degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
degree_count = nx.degree_histogram(G)
plt.bar(range(len(degree_count)), degree_count, width=0.8, color='b')
plt.xlabel('Degree')
plt.ylabel('Count')
plt.title('Degree Distribution')
plt.show()

# Size of the largest connected component
largest_cc = max(nx.connected_components(G), key=len)
print("Size of the largest connected component:", len(largest_cc))

# Distance distribution
distance_dict = dict(nx.all_pairs_shortest_path_length(G))
distances = []
for source, targets in distance_dict.items():
    distances.extend(list(targets.values()))
distance_count = nx.degree_histogram(distances)
plt.bar(range(len(distance_count)), distance_count, width=0.8, color='b')
plt.xlabel('Distance')
plt.ylabel('Count')
plt.title('Distance Distribution')
plt.show()

# Clustering coefficient
clustering_coefficient = nx.average_clustering(G)
print("Clustering coefficient:", clustering_coefficient)

# Betweenness centrality
betweenness_dict = nx.betweenness_centrality(G)
betweenness_values = list(betweenness_dict.values())
plt.hist(betweenness_values, bins=20, color='b', alpha=0.7)
plt.xlabel('Betweenness Centrality')
plt.ylabel('Count')
plt.title('Betweenness Centrality Distribution')
plt.show()
