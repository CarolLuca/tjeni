from sklearn.feature_extraction.text import CountVectorizer

def directional_jaccard_containment(p1, p2, ngram_range=(1, 1)):
    # Tokenize and create n-grams for each paragraph separately
    vectorizer = CountVectorizer(ngram_range=ngram_range, analyzer='word')
    
    # Get the n-grams as sets of features (unique words or phrases)
    p1_ngrams = set(vectorizer.fit([p1]).get_feature_names_out())
    p2_ngrams = set(vectorizer.fit([p2]).get_feature_names_out())
    
    # Calculate directional containment
    def containment_score(ngrams1, ngrams2):
        intersection = len(ngrams1.intersection(ngrams2))
        return intersection / len(ngrams1) if len(ngrams1) != 0 else 0

    # Proportion of p1's n-grams found in p2 (p1 contained in p2)
    containment_p1_in_p2 = containment_score(p1_ngrams, p2_ngrams)
    # Proportion of p2's n-grams found in p1 (p2 contained in p1)
    containment_p2_in_p1 = containment_score(p2_ngrams, p1_ngrams)

    return containment_p1_in_p2, containment_p2_in_p1

# Example usage
p1 = "The cat sat on the mat."
p2 = "The cat is sitting on the mat with a hat."

containment_p1_in_p2, containment_p2_in_p1 = directional_jaccard_containment(p1, p2)
print(f"Containment Score (p1 in p2): {containment_p1_in_p2:.3f}")
print(f"Containment Score (p2 in p1): {containment_p2_in_p1:.3f}")
