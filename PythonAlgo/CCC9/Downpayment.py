def savingsduration(annualsalary, percentagesaved, totalcost, payraise):
    currentSavings = 0.0
    currentMonth = 1
    while (currentSavings < totalcost * 0.25):
        currentMonth += 1
        if currentMonth > 0 and currentMonth % 6 == 0:
            annualsalary *= (1.0 + payraise)
        currentSavings += annualsalary * percentagesaved / 12.0
        if currentMonth > 0 and currentMonth % 12 == 0:
            currentSavings *= 1.04
    return currentMonth

print(savingsduration(120000, 0.05, 500000, 0.03))

