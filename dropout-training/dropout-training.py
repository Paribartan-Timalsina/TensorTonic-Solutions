import numpy as np

def dropout(
    x: list,
    p: float = 0.5,
    rng: np.random.Generator = None,
) -> tuple[np.ndarray, np.ndarray]:

    x = np.array(x)

    mask = rng.random(x.shape) >= p

    scale = 1 / (1 - p)

    output = x * mask * scale
    dropout_pattern = mask * scale

    return output, dropout_pattern