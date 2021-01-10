
def RecurFactorio(n):
    if n == 1:
        return 1
    return n * RecurFactorio(n - 1)

print(RecurFactorio(6))

