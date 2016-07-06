def checkio(number):
    result = 0
    for i in bin(number):
        if i == "1": 
            result += 1
    return result 
