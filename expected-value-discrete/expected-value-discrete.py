import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    x = np.array(x)
    p = np.array(p)

    if len(x) != len(p):
        raise ValueError("Not Equal Length")

    if not np.isclose(np.sum(p),1):
        raise ValueError("Probabability Sum should be 1")
        
    return np.dot(x,p)
