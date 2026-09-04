import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    x = np.array(x)
    y = np.array(y)
    distance = np.sum(abs(x-y))
    return float(distance)