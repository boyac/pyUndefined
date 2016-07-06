OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):
    if operation == 'conjunction':
        if x and y:
            return 1
        else:
            return 0
    elif operation == 'disjunction':
        if x or y:
            return 1
        else:
            return 0
    elif operation == 'implication':
        if x:
            return y
        else:
            return 1
    elif operation == 'exclusive':
        if x == y:
            return 0
        else:
            return 1
    elif operation == 'equivalence':
        if x == y:
            return 1
        else:
            return 0
    return 1 or 0
