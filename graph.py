from sklearn.feature_extraction.text import CountVectorizer
from functools import lru_cache
from typing import NamedTuple

CACHE_SIZE = 128


class Edge(NamedTuple):
    src: str
    dest: str
    cost: int


class DSU:
    def __init__(self, size):
        self.size = size
        self.link = [i for i in range(self.size)]
        self.dim = [1] * self.size

    def get_father(self, x):
        aux = x
        while aux != self.link[aux]:
            aux = self.link[aux]
        cpy = x
        while cpy != self.link[cpy]:
            lst = cpy
            cpy = self.link[cpy]
            self.link[lst] = aux
        return aux

    def unite(self, x, y):
        gx = self.get_father(x)
        gy = self.get_father(y)
        if gx == gy:
            return False

        if self.dim[gx] < self.dim[gy]:
            gx, gy = gy, gx

        self.dim[gx] += self.dim[gy]
        self.link[gy] = gx

        return True


class Graph:
    def __init__(self, size):
        self.size = size
        self.edges = []

    def add_edge(self, i, j, c):
        self.edges.append(Edge(src=i, dest=j, cost=c))

    def mst(self):
        selected_edges = []
        self.edges.sort(key=lambda edge: edge.cost, reverse=True)
        dsu = DSU(self.size)
        for edge in self.edges:
            if dsu.unite(edge.src, edge.dest):
                selected_edges.append(edge)

        self.edges = selected_edges


@lru_cache(maxsize=CACHE_SIZE)
def get_ngrams(vectorizer, paragraph):
    return set(vectorizer.fit([paragraph]).get_feature_names_out())


def containment_score(ngrams1, ngrams2):
    intersection = len(ngrams1.intersection(ngrams2))
    return intersection / len(ngrams1) if len(ngrams1) != 0 else 0


def compute_graph(paragraphs):
    vectorizer = CountVectorizer(ngram_range=(1, 1), analyzer="word")

    def directional_jaccard_containment(id_p1, id_p2):
        p1 = paragraphs[id_p1]
        p2 = paragraphs[id_p2]

        p1_ngrams = get_ngrams(vectorizer, p1)
        p2_ngrams = get_ngrams(vectorizer, p2)

        containment_p1_in_p2 = containment_score(p1_ngrams, p2_ngrams)
        containment_p2_in_p1 = containment_score(p2_ngrams, p1_ngrams)

        return containment_p1_in_p2, containment_p2_in_p1

    block_count = (len(paragraphs) + CACHE_SIZE - 1) // CACHE_SIZE
    graph = Graph(len(paragraphs))

    for bi in range(block_count):
        for bj in range(block_count):
            li = bi * CACHE_SIZE
            ri = min((bi + 1) * CACHE_SIZE, len(paragraphs))
            lj = bj * CACHE_SIZE
            rj = min((bj + 1) * CACHE_SIZE, len(paragraphs))
            for i in range(li, ri):
                for j in range(lj, rj):
                    if i < j:
                        cij, cji = directional_jaccard_containment(i, j)
                        graph.add_edge(i, j, min(max(cij, cji), 1 - min(cij, cji)))

    graph.mst()
    return graph
