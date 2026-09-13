import numpy as np

def apply_causal_mask(scores: list, mask_value: float = -1e9) -> np.ndarray:
    scores = np.array(scores)

    rows, columns = scores.shape[-2:]

    i = np.arange(rows)[:, None]
    j = np.arange(columns)[None, :]

    mask = i < j

    scores = np.where(mask, mask_value, scores)

    return scores