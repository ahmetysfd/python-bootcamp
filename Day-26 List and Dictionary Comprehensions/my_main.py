import csv

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

user_input = input("Enter a name: ")
letter_list = list(user_input.upper())

phonetic_dict = {}

with open("nato_phonetic_alphabet.csv", mode="r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        letter, code = row  # Unpack the values from each row
        phonetic_dict[letter] = code  # Store in dictionary

result_dict = {letter: phonetic_dict[letter] for letter in letter_list if letter in phonetic_dict}


print(result_dict)

