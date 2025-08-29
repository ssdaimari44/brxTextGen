from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def cluster_relations(triples, num_clusters=20):
    # Input: list of (subj, rel, obj)
    relation_strings = [rel for (_, rel, _) in triples]
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(relation_strings)

    kmeans = KMeans(n_clusters=num_clusters, random_state=42).fit(X)
    clusters = {i: [] for i in range(num_clusters)}
    for idx, label in enumerate(kmeans.labels_):
        clusters[label].append(relation_strings[idx])
    return clusters
