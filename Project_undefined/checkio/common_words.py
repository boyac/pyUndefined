def checkio(first, second):
    a = set(first.split(","))
    b = set(second.split(","))
    result = sorted(a & b)
    return ",".join(result)
