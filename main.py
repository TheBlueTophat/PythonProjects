
import string
import random
#import my_functions

#random_number = random.randint(0, 23)
#print(string.ascii_uppercase[random_number])

vowels = ["A", "E", "I", "O", "U"]

vowels_dict = {
    "A": 0,
    "E": 1,
    "I": 2,
    "O": 3,
    "U": 4
}

alphabet = list(string.ascii_uppercase)

alphabet_dict = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9,
    "K": 10,
    "L": 11,
    "M": 12,
    "N": 13,
    "O": 14,
    "P": 15,
    "Q": 16,
    "R": 17,
    "S": 18,
    "T": 19,
    "U": 20,
    "V": 21,
    "W": 22,
    "X": 23,
    "Y": 24,
    "Z": 25
}

def generate_dictionary(keys, values):
    print("NAME = {")
    for i in range(len(keys)):
        endline_char = "," if i + 1 in range(len(keys)) else ""
        print(f"    \"{keys[i]}\": {values[i]}{endline_char}")
            
    print("}")

#generate_dictionary(string.ascii_uppercase, range(0, 26))

#generate_dictionary(vowels, range(len(vowels)))

consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

def find_consonants():
    consonants_wip = []
    for letter in alphabet:
        if letter not in vowels:
            consonants_wip.append(letter)

    print(consonants_wip)

def generate_word(template):
    word = []
    for i in template:
        if(i == "V"):
            word.append(vowels[random.randint(0, len(vowels) - 1)])
        elif(i == "C"):
            word.append(consonants[random.randint(0, len(consonants) - 1)])
        elif(i == "|"):
            char_set = random.choice([vowels, consonants])
            word.append(char_set[random.randint(0, len(char_set) - 1)])
        elif(i == "%"):
            char_set = random.choice([vowels, consonants, [""]])
            word.append(random.choice(char_set))

    print(''.join(word))

for i in range(10):
    print(generate_word("C%%VC"))

