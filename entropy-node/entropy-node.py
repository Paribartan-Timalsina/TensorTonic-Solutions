import numpy as np

def entropy_node(y):
    y = np.array(y)

    # compute frequency of each class
    values, counts = np.unique(y, return_counts=True)
    probs = counts / len(y)

    return -np.sum(probs * np.log2(probs))