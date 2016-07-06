VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
PUNCTUATION = ",.!?"
​
def checkio(text):
    text = text.upper()
    for c in PUNCTUATION:
        text = text.replace(c, " ")
    for c in VOWELS:
        text = text.replace(c, "v")
    for c in CONSONANTS:
        text = text.replace(c, "c")
        
    words = text.split(" ")
    count = 0 
    for word in words:
        if len(word) > 1 and word.isalpha():
            if 'c'*2 not in word and 'v'*2 not in word:
                count += 1
    return count
