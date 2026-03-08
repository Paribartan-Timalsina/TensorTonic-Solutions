def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    new_x = x0
    for i in range(steps):
        new_x = new_x - lr * (2*a*new_x + b)
    return new_x