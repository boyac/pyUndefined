def checkio(number):
    result = 1
    for s in str(number):
        n = int(s)
        if n >0:
            result *= n
    return result
