def count_inversion(sequence):
    """
        Count inversions in a sequence of numbers
    """
    count = 0
    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence)):
            if sequence[i] > sequence[j]:
                count += 1
    return count 
