def QuaterbackRating(attempts, comps, yards, tdowns, ints):
    scores = []
    scores.append((1.0 * comps / attempts - 0.3) * 5)
    scores.append((1.0 * yards / attempts - 3) * 0.25)
    scores.append((20.0 * tdowns / attempts))
    scores.append((2.375 - (25.0 * ints / attempts)))
    total = 0
    for i in range(len(scores)):
        if scores[i] > 2.375:
            scores[i] = 2.375
        elif scores[i] < 0:
            scores[i] = 0
        total += scores[i]
        # scores[i] = 2.375 if scores[i] > 2.375 else scores[i] = 0.0 if scores[i] < 0 else scores[i] = scores[i]
    return (total / 6.0) * 100
print(QuaterbackRating(35, 26, 235, 2, 1))