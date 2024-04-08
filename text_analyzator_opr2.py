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
    exit()

print(f"Welcome to the app, {user}")
print("We have 3 texts to be analyzed")
print("-" * 40)

number = input("Enter a number btw. 1 and 3 to select: ")
count_text = len(task_template.TEXTS)

if not number.isdigit():
    print("This is not a number, terminating program... ")
    exit()
elif int(number) > count_text or int(number) <= 0:
    print("This number is not in range, terminating program...")
    exit()

print("-" * 40)
selected_text = task_template.TEXTS[int(number) - 1]


# statistiky

stats = {"titlecase": 0, "uppercase": 0, "lowercase": 0, "count_num": 0, "sum_num": 0}
word_lengths = {}
text = selected_text.replace(",", "").replace(".", "")
for word in text.split():
    length = len(word)
    word_lengths[length] = word_lengths.get(length, 0) + 1
    if word[0].isupper():
        stats["titlecase"] += 1
    if word.isupper() is True and word.isalpha() is not True and word.isdigit() is not True:
        stats["uppercase"] += 1
    if word.islower():
        stats["lowercase"] += 1
    if word.isdigit():
        stats["count_num"] += 1
        stats["sum_num"] = int(word) + stats["sum_num"]

print(f"There are {len(selected_text.split())} words in the selected text.")
print(f'There are {stats["titlecase"]} titlecase words.')
print(f"There are {stats["uppercase"]} uppercase words.")
print(f"There are {stats["lowercase"]} lowercase words.")
print(f"There are {stats["count_num"]} numeric string.")
print(f"The sum of all the numbers {stats["sum_num"]}.")

# sloupcovy_graf
print("-" * 40)
print(f"{"LEN":^3} | {"OCCURENCES":^20}| {"NR."}")
print("-" * 40)

for key, value in sorted(word_lengths.items()):
    occur = "*" * value
    print(f" {key:^3}| {occur:<20}| {value}")
