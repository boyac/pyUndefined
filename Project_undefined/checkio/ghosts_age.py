def fibo():
    a, b = 0, 1
    fibo = [a, b]
    while a+b < 5000:
        a, b = b, a+b
        fibo.append(b)
    return fibo
    
def checkio(opacity):
    cur_op = 10000
    age = 0
    while opacity != cur_op:
        age += 1
        if age in fibo():
            cur_op -= age
        else:
            cur_op += 1
    return age
