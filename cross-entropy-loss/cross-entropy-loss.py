import numpy as np

def cross_entropy_loss(y_true: list[int], y_pred: list[list[float]]) -> float:
    """
    Returns the mean multiclass cross-entropy loss as a Python float.
    """
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    filtered_probabilities = y_pred[np.arange(len(y_pred)), y_true]
    
    loss = np.log(filtered_probabilities) * -1
    summation = np.sum(loss)
    return summation/len(y_true)
    