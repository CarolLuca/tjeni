import networkx as nx
from node2vec import Node2Vec


def convert_graph(paragraphs, graph):
    G = nx.DiGraph()
    for i in range(graph.size):
        G.add_node(i, text=paragraphs[i])
    for edge in graph.edges:
        G.add_edge(edge.src, edge.dest)

    return G


def compute_embeddings(paragraphs, graph):
    G = convert_graph(paragraphs, graph)
    node2vec = Node2Vec(G, dimensions=64, walk_length=30, num_walks=200, workers=4)
    model = node2vec.fit(window=10, min_count=1, batch_words=4)
    embeddings = {node: model.wv[node] for node in G.nodes()}
    return embeddings
