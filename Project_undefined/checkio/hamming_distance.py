def checkio(n, m):
    n = '{:08b}'.format(n).zfill(20)
    m = '{:08b}'.format(m).zfill(20)
    # most of my time stuck at solving the unblanced number of bits
    
    count = 0
    for i, j in zip(n, m):
        if i != j:
            count += 1
    return count
