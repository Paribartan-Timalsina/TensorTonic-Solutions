def f1_micro(y_true: list[int], y_pred: list[int]) -> float:
    """
    Returns the micro-averaged F1 score as a Python float rounded to four decimals.
    """
    # Write code here
    true_positive = 0
    false_positive = 0
    false_negative = 0

    for i in range(len(y_true)):
        if y_true[i] == y_pred[i]:
            true_positive+=1
        else:
            false_positive +=1

    false_negative = false_positive
    return round((2*true_positive)/(2*true_positive+false_negative+false_positive), 4)
            