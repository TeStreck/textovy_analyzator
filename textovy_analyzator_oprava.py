"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Tereza Streckerová
email: tereza.vack@gmail.com
discord: te.str
"""
# import textů ze souboru, proměnná TEXTS obsahuje jednotlivé texty
import task_template

users = {"bob": "123", "ann": "pas123", "mike": "password123", "liz": "pas123"}

user = input("Vlož přihlašovací jméno: ")
password = input("Vlož heslo: ")


if users.get(user) != password:
    print("Unregistered user, terminating the program...")
else:
    print(f"Welcome to the app, {user}")
    print("We have 3 texts to be analyzed")

    print("-" * 40)

    number = input("Enter a number btw. 1 and 3 to select: ")
    count_text = len(task_template.TEXTS)

    if number.isalpha() or not number.isdigit():
        print("This is not a number, terminating program... ")

    elif int(number) > count_text or int(number) <= 0:
        print("This number is not in range, terminating program...")

    else:
        print("-" * 40)
        selected_text = task_template.TEXTS[int(number) - 1]


        # statistiky
        stat_2 = 0
        stat_3 = 0
        stat_4 = 0
        stat_5 = 0
        stat_6 = 0

        stats = {"stat_2": 0, "stat_3": 0, "stat_4": 0, "stat_5": 0, "stat_6": 0}

        for word in selected_text.split():
            if word[0].isupper():
                stats["stat_2"] += 1
            if word.isupper() is True and word.isalpha() is not True and word.isdigit() is not True:
                stat_3 += 1
            if word.islower():
                stat_4 += 1
            if word.isdigit():
                stat_5 += 1
                stat_6 += int(word) + stat_6

        print(f"There are {len(selected_text.split())} words in the selected text.")
        print(f'There are {stats["stat_2"]} titlecase words.')
        print(f"There are {stats["stat_3"]} uppercase words.")
        print(f"There are {stats["stat_4"]} lowercase words.")
        print(f"There are {stats["stat_5"]} numeric string.")
        print(f"The sum of all the numbers {stats["stat_6"]}.")

        # sloupcovy_graf
        print("-" * 40)
        print(f"{"LEN":^3} | {"OCCURENCES":^20}| {"NR."}")
        print("-" * 40)

        repl_text = selected_text.replace(",", "").replace(".", "")

        freq = [len(word) for word in list(repl_text.split())]

        counts = {}
        for f_num in freq:
            if f_num not in counts:
                counts[f_num] = 1
            else:
                counts[f_num] = counts[f_num] + 1
        for key, value in sorted(counts.items()):
            occur = "*" * value
            print(f" {key:^3}| {occur:<20}| {value}")

