import networkx as nx
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Sample data (paragraphs)
paragraphs = [
    "This is the first paragraph, introducing the main topic.",
    "The second paragraph elaborates on the first paragraph's topic.",
    "This section presents a related but distinct topic.",
    "A deep dive into the main topic, providing more specifics.",
    "An entirely different topic unrelated to the previous sections.",
]

# Step 1: Compute TF-IDF vectors and similarity matrix
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(paragraphs)
similarity_matrix = cosine_similarity(tfidf_matrix)

# Step 2: Create a Graph and Add Nodes
G = nx.DiGraph()
for i, para in enumerate(paragraphs):
    G.add_node(i, text=para)

# Step 3: Add Edges Based on Similarity (Threshold-based for hierarchy)
threshold = 0.3  # Adjust this for stricter or looser hierarchy
for i in range(len(paragraphs)):
    for j in range(i + 1, len(paragraphs)):
        if similarity_matrix[i][j] > threshold:
            G.add_edge(i, j)

# Step 4: Plot the Graph
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G)
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=3000,
    node_color="lightblue",
    font_size=10,
    font_weight="bold",
)
node_labels = {i: para[:30] + "..." for i, para in enumerate(paragraphs)}
nx.draw_networkx_labels(G, pos, labels=node_labels)
plt.show()
