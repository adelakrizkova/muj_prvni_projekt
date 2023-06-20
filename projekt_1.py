'''
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Adéla Křížková
email: adela.krizkova@karlinblok.cz
discord: Adule
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}
name = input("Username: ")
if name not in users.keys():
    print("Unregistered user, terminating the program...")
    quit()
else:
    password = input("Password: ")
if password.__str__() != users[name]:
    print("Wrong password, terminating the program...")
    quit()
else:
    print("-" * 40)
    print("Welcome to the app,", name, "\nWe have 3 texts to be analized.")
    print("-" * 40)
text_number = input("Enter a number btw. 1 and 3 to select: ")
if int(text_number) > 3 or int(text_number) < 1:
    print("You must enter number btw. 1 and 3, terminating the program...")
    quit()
else:
    print("-" * 40)
    text = (TEXTS[int(text_number)-1])
    text_split = text.split()

    word_count = len(text_split)
    print("There are", word_count, "words in the selected text.")

    words_titlecase = []
    for word in text_split:
        if word.istitle():
            words_titlecase.append(word)
    titlecase = len(words_titlecase)
    print("There are", titlecase, "titlecase words.")

    words_uppercase = []
    for word in text_split:
        if word.isupper():
            words_uppercase.append(word)
    uppercase = len(words_uppercase)
    print("There are", uppercase, "uppercase words.")

    words_lowercase = []
    for word in text_split:
        if word.islower():
            words_lowercase.append(word)
    lowercase = len(words_lowercase)
    print("There are", lowercase, "lowercase words.")

    words_numeric = []
    for word in text_split:
        if word.isnumeric():
            words_numeric.append(word)
    numeric = len(words_numeric)
    print("There are", numeric, "numeric strings.")
    numeric_int = []
    for number in words_numeric:
        numeric_int.append(int(number))
    sum_numeric = sum(numeric_int)
    print("The sum of all the numbers", sum_numeric)
    print("-" * 40)

    shortest_word = text_split[0]
    for short_word in text_split:
        if len(short_word) < len(shortest_word):
            shortest_word = short_word
    longest_word = text_split[0]
    for long_word in text_split:
        if len(long_word) > len(longest_word):
            longest_word = long_word
    word_min = len(shortest_word)
    word_max = len(longest_word)

    print("LEN  | OCCURENCES       |NR.")

    word_len = word_min
    while word_len <= word_max:
        list_words = []
        for words in text_split:
            if len(words) == word_len:
                list_words.append(words)
        if len(list_words):
            word_len_str = str(word_len)
            print(word_len_str + " " * (5 - len(word_len_str)) + "|"
                + "*" * len(list_words) + " " * (18 - len(list_words))
                + "|" + str(len(list_words))
                )
        word_len += 1






