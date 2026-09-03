import numpy as np

def positional_encoding(seq_len: int, d_model: int, base: float = 10000.0) -> np.ndarray:
    array = np.zeros((seq_len, d_model))

    for pos in range(seq_len):
        for j in range(d_model):
            i = j // 2

            power_term = (2 * i) / d_model
            denom = base ** power_term

            if j % 2 == 0:
                array[pos][j] = np.sin(pos / denom)
            else:
                array[pos][j] = np.cos(pos / denom)

    return array