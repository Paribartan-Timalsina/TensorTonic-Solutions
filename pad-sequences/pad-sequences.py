import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    # here what I need to do is fill all the seqs with pad_value in right upto max_len. If some is greater than max_len truncate it

    if max_len is None:
        max_len = max((len(seq) for seq in seqs), default=0)
    output = np.full((len(seqs), max_len), pad_value)

    for i, seq in enumerate(seqs):
        min_length = min(len(seq), max_len)
        output[i, :min_length] = seq[:min_length]

    return output
        
    