def check_pangram(text):
    t = text.lower() 
    count = 0
    for i in range(97,123):
        # range(97,123) is the ascii table of alphbet from a-z
        if chr(i) in t: 
            count += 1 
    if count == 26: 
        return True 
    else: 
        return False
