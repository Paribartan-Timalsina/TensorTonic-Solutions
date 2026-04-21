import numpy as np

def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    recommended = np.array(recommended[:k])
    relevant = np.array(relevant)

    # Check which recommended items are relevant
    hits = np.isin(recommended, relevant)

    # Count relevant items in top-k
    count = np.sum(hits)

    precision = count / k
    recall = count / len(relevant) if len(relevant) > 0 else 0

    return [precision, recall]