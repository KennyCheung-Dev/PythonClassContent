'''
Farmer John's cows are excited to learn that Chinese New Year was recently celebrated,
ushering in the year of the Ox, always a bovine favorite.
As we know, the zodiac animals for Chinese calendar years follow a 12-year cycle:
Ox, Tiger, Rabbit, Dragon, Snake, Horse, Goat, Monkey, Rooster, Dog, Pig, Rat,
 and then Ox again.

Bessie the cow is proud to say she was born in a year of the Ox, many years ago.
Her friend Elsie wants to know how many years apart from Bessie she was born,
and hopes you can help her deduce this by looking at relationships between
the birth years of several cows on the farm.

INPUT FORMAT (input arrives from the terminal / stdin):
The first line of input contains an integer N (1≤N≤100).
Each of the next N lines contains an 8-word phrase specifying
the relationship between the birth years of two cows.
It is of the form
"Mildred born in previous Dragon year from Bessie",

or

"Mildred born in next Dragon year from Bessie"



The last word is the name of a cow on the farm, which is either "Bessie" or
a cow that has already been mentioned in a previous line of input.

The first word is the name of a cow on the farm who is not "Bessie" and
who has not yet been mentioned in the input. All cow names have at most
10 characters that are in the range a..z or A..Z.

The 5th word is one of the 12 zodiac animals above.

The 4th word is either "previous" or "next". For example, if the phrase is
"Mildred born in previous Dragon year from Bessie",
then Mildred's year of birth was the Dragon year closest to and
strictly before (not equal to) Bessie's birth year.

OUTPUT FORMAT (print output to the terminal / stdout):
Please output the number of years by which Bessie and Elsie's birth years differ.
It is guaranteed that this number can be determined by the input given.
SAMPLE INPUT:
4
Mildred born in previous Dragon year from Bessie
Gretta born in previous Monkey year from Mildred
Elsie born in next Ox year from Gretta
Paulina born in next Dog year from Bessie
SAMPLE OUTPUT:
12
In the input above,

Elsie was born 12 years before Bessie.
Mildred was born 9 years before Bessie.
Gretta was born 17 years before Bessie.
Paulina was born 9 years after Bessie.
Problem credits: Brian Dean
'''



n = int(input())

animals = ["Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig", "Rat"]
data = {
    "Bessie" : [0, "Ox"]
}
def ComputeYearDifference(animalGuessing, animalReference, direction):
    animalGuessingIndex = animals.index(animalGuessing)
    animalReferenceIndex = animals.index(animalReference)
    difference = animalGuessingIndex - animalReferenceIndex
    if direction == "next" and animalGuessingIndex <= animalReferenceIndex:
        animalGuessingIndex += 12
    if direction == "previous" and animalGuessingIndex >= animalReferenceIndex:
        animalGuessingIndex -= 12

    return animalGuessingIndex - animalReferenceIndex

for i in range(n):
    line = input().split()
    guessing = line[0]
    reference = line[-1]
    direction = line[3]
    guessingAnimal = line[4]
    referenceAnimal = data[reference][1]
    ageDifference = ComputeYearDifference(guessingAnimal, referenceAnimal, direction)
    age = data[reference][0] + ageDifference
    data[guessing] = [age, guessingAnimal]

ageDiffBessieElsie = abs(data["Bessie"][0] - data["Elsie"][0])
print(ageDiffBessieElsie)

