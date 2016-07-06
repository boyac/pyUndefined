def checkio(words):
    count = 0    
    for w in words.split():
        if w.isalpha():
            count += 1
            if count >= 3:
                break
        else:
            count = 0
    
    if count >= 3:
        return True
    else: 
        return False
