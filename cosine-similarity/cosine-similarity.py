import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    a_new = np.linalg.norm(a)
    b_new = np.linalg.norm(b)
    if a_new == 0 or b_new == 0:
        return float(0)
    c_new = np.dot(a,b)
    return float(c_new/(a_new*b_new))
    