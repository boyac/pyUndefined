def find_message(text):
    """Find a secret message"""
    word = ""
    for t in text: 
        if t.isupper() == True:
            word += t
    return word
