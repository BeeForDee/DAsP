"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Barbora Pitašová
email: bpitasova@gmail.com
"""

#Texty ke zpracovani
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

#Registrovani uzivatele
register_users = {
    "bob" : "123",
    "ann" : "pass123",
    "mike" : "password123",
    "liz" : "pass123"
}

#Zadani prihlasovacich udaju od uzivatele
user_name = input("username:")
password = input("password:")

#Promene s nulou k pocitani
title_lst = 0
upper_lst = 0
lower_lst = 0
digit_lst = 0
number_lst = 0

#Prazndy list pro pocitani delky slov
lngth_lst = []

#Specialni znaky pro odebrani ze stringu
special_characters = '-.,:!?'

#Overeni uzivatele
if register_users.get(user_name) == password:
    #Uvodni text
    print("{:<40}".format("-" * 40))
    print("{:<40}".format("Welcome to the app {}.\nWe have 3 texts to be analyzed.".format (user_name)))
    print("{:<40}".format("-" * 40))
    text_number = input("Enter a number btw. 1 and 3 to select:")
    print("{:<40}".format("-" * 40))
   
    #Text prvni
    if text_number == "1":
        text_words = TEXTS[0].split()

        #01 pocet slov v textu
        words_cnt = len(text_words)

        #02 pocet slov s pocatecnimi velkymi pismeny
        for word in text_words:
            if word.istitle():
                title_lst += 1

        #03 pocet slov s velkymi pismeny (Pocita i cisla)
            if word.isupper() and word.isalpha():
                upper_lst += 1

        #04 pocet slov s malymi pismeny
            if word.islower():
                lower_lst += 1     

        #05 pocet slov s cisly
            if word.isdigit():
                digit_lst += 1          

        #06 soucet vsech cisel v textu
            if word.isdigit():
                number_lst += int(word)

        #vystupy
        print("There are {} words in the selected text.".format(words_cnt))

        print("There are {} titlecase words.".format (title_lst))

        print("There are {} uppercase words.".format (upper_lst))

        print("There are {} lowercase words.".format (lower_lst))

        print("There are {} numeric strings.".format (digit_lst))

        print("The sum of all the numbers {}.".format (number_lst))

        print("{:<40}".format("-" * 40))
        print("{:<4}".format("LEN|"), "{:^13}|".format("OCCURENCES"), "{:<}".format("|NR." ))
        print("{:<40}".format("-" * 40))

        #pocet znaku ve slove
        for word in text_words:
            lngth_word = len(word.strip(special_characters))
            lngth_lst.append(lngth_word)

        mx_lngth_lst = max(lngth_lst)

        for number in range(1,  mx_lngth_lst+1):
            z = lngth_lst.count(number)
            print("{:<3}|".format(number), "{:<13}|".format("*" * z), "{:<}".format(z))

    elif text_number == "2":
        text_words = TEXTS[1].split()

        #01 pocet slov v textu
        words_cnt = len(text_words)

        #02 pocet slov s pocatecnimi velkymi pismeny
        for word in text_words:
            if word.istitle():
                title_lst += 1

        #03 pocet slov s velkymi pismeny (Pocita i cisla)
            if word.isupper() and word.isalpha():
                upper_lst += 1

        #04 pocet slov s malymi pismeny
            if word.islower():
                lower_lst += 1     

        #05 pocet slov s cisly
            if word.isdigit():
                digit_lst += 1          

        #06 soucet vsech cisel v textu
            if word.isdigit():
                number_lst += int(word)

        #vystupy
        print("There are {} words in the selected text.".format(words_cnt))

        print("There are {} titlecase words.".format (title_lst))

        print("There are {} uppercase words.".format (upper_lst))

        print("There are {} lowercase words.".format (lower_lst))

        print("There are {} numeric strings.".format (digit_lst))

        print("The sum of all the numbers {}.".format (number_lst))

        print("{:<40}".format("-" * 40))
        print("{:<4}".format("LEN|"), "{:^13}|".format("OCCURENCES"), "{:<}".format("|NR." ))
        print("{:<40}".format("-" * 40))

        #pocet znaku ve slove
        for word in text_words:
            lngth_word = len(word.strip(special_characters))
            lngth_lst.append(lngth_word)

        mx_lngth_lst = max(lngth_lst)

        for number in range(1,  mx_lngth_lst+1):
            z = lngth_lst.count(number)
            print("{:<3}|".format(number), "{:<13}|".format("*" * z), "{:<}".format(z))

    elif text_number == "3":
        text_words = TEXTS[2].split()

        #01 pocet slov v textu
        words_cnt = len(text_words)

        #02 pocet slov s pocatecnimi velkymi pismeny
        for word in text_words:
            if word.istitle():
                title_lst += 1

        #03 pocet slov s velkymi pismeny (Pocita i cisla)
            if word.isupper() and word.isalpha():
                upper_lst += 1

        #04 pocet slov s malymi pismeny
            if word.islower():
                lower_lst += 1     

        #05 pocet slov s cisly
            if word.isdigit():
                digit_lst += 1          

        #06 soucet vsech cisel v textu
            if word.isdigit():
                number_lst += int(word)

        #vystupy
        print("There are {} words in the selected text.".format(words_cnt))

        print("There are {} titlecase words.".format (title_lst))

        print("There are {} uppercase words.".format (upper_lst))

        print("There are {} lowercase words.".format (lower_lst))

        print("There are {} numeric strings.".format (digit_lst))

        print("The sum of all the numbers {}.".format (number_lst))

        print("{:<40}".format("-" * 40))
        print("{:<4}".format("LEN|"), "{:^13}|".format("OCCURENCES"), "{:<}".format("|NR." ))
        print("{:<40}".format("-" * 40))

        #pocet znaku ve slove
        for word in text_words:
            lngth_word = len(word.strip(special_characters))
            lngth_lst.append(lngth_word)

        mx_lngth_lst = max(lngth_lst)

        for number in range(1,  mx_lngth_lst+1):
            z = lngth_lst.count(number)
            print("{:<3}|".format(number), "{:<13}|".format("*" * z), "{:<}".format(z))
    else:
        print("Vyber nerozeznan. Program bude ukoncen.")
        exit()

else:
    print("unregistered user, terminating the program..")