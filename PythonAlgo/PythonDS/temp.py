'''
1. Given a string, return a string where for every character
in the original, there are two characters

double_char('The') -> 'TThhee'
double_char('AAbb') -> 'AAAAbbbb'
double_char('Hi-There') -> 'HHii--TThheerree'

#Answer
def double_char(str):
    result = ''
    for i in str:
        result += i * 2
    return result

2. Return the number of times that the string "hi" appears anywhere
in the give nstring.

count_hi('abc hi ho') -> 1
count_hi('ABChi hi') -> 2
count_hi('hihi') -> 2

# Answer
# def count_code(str):
#     count = 0
#     for char in 'abcdefghijklmnopqrstuvwxyz':
#         count += str.count('co{}{}'.format(char, 'e'))
#     return count


3. Return The if the string "cat" and "dog" appear the same number of times
in the given string.
cat_dog('catdog') -> True
cat_dog('catcat') -> False
cat_dog('1cat1cadodog') -> True

# Answer
def cat_dog(str):
    c = str.count('cat')
    d = str.count('dog')
    if c == d:
        return True
    else:
        return False

'''

#Explanation to fString
# num = 10
# print("abc{}de".format(num))
#
# print(f'abc{10}de')


# def convert_to_maderin(num):
#     pass


#Explanations on Dictionary
num = {
    '0' : 'ling',
    '1' : 'yi',
    '2' : 'er'
}

# Adding a key value pair into dict
num['3'] = 'san'

# Access a value with a key
print(num['3'])

# Loop through all keys and values inside
for (key, value) in num.items(): #key value pairs
    print(key + " " + value)



