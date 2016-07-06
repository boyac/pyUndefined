def checkio(words):
        if len(words) <= 1:
            return False
        else:
            for w1 in words:
                for w2 in words:
                    if w1 == w2:
                        continue
                    elif w1.endswith(w2):
                        return True
        return False
