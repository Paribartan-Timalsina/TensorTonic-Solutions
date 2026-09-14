import numpy as np

def get_alpha_bar(betas: list[float]) -> list[float]:
    """
    Returns the cumulative alpha-bar values rounded to six decimals.
    """
    betas = np.array(betas)
    return np.cumprod(1-betas)

def forward_diffusion(x_0: list, t: int, betas: list[float], epsilon: list) -> list:
    """
    Returns x_t with the same nested shape as x_0.
    """
    alpha_bar = get_alpha_bar(betas)
    root_alpha_bar = alpha_bar**0.5
    root_one_minus_alpha_bar = (1-alpha_bar)**0.5
    root_alpha_bar_at_t = root_alpha_bar[t-1]
    root_one_minus_alpha_bar_at_t = root_one_minus_alpha_bar[t-1]
    return list(root_alpha_bar_at_t * np.array(x_0) + root_one_minus_alpha_bar_at_t * np.array(epsilon))
    
    
    