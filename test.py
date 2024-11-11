from graph import compute_graph
from embeddings import compute_embeddings


def test():
    paragraphs = [
        "The house is on fire",
        "There is a cat",
        "The cat outside is smilling",
        "The cat species is a really developed kind that is able to smile",
    ]

    graph = compute_graph(paragraphs)

    for edge in graph.edges:
        print(edge)

    embeddings = compute_embeddings(paragraphs, graph)
    print(embeddings[0])


if __name__ == "__main__":
    test()
