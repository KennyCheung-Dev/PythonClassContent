num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in num:
    for j in num:
        for k in num:
            for l in num:
                if i != j != k != l:
                    if i + j == k * l and i * j == k + l:
                        print("One result : ", i, j, k, l)