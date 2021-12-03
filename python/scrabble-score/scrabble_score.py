SCORES = {"AEIOULNRST": 1, "DG": 2, "BCMP": 3, "FHVWY": 4, "K": 5, "JX": 8, "QZ": 10}

def score(word):
    score = 0
    for letter in word.upper():
        for key in SCORES.keys():
            if letter in key:
                score = score + SCORES.get(key)
    return score
