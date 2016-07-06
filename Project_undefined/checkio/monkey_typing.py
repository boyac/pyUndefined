def count_words(text, words):
    count = 0
    for i in words:
        if i in text.lower():
            count += 1
    return count
