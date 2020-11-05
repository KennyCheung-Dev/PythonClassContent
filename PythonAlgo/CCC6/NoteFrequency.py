# s = input().split(".")
# frequency = 440 * (2 ** (int(s[0]) - 4 + ((int(s[1]) - 9) / 12)))
# print(frequency)


def NoteFrequency(a, b):
    return 440 * (2 ** (a - 4 + ((b - 9) / 12)))

print(NoteFrequency(-4, 0))