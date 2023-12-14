"""
gd
"""
import datetime
import language_module

LANGUAGE = "čeština"

def load_questions(file_path):
    """
    FD
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    questions = [line.strip() for line in lines if line.strip()]
    return [questions[i:i + 6] for i in range(0, len(questions), 6)]

def question(question_set):
    """
    FG
    """
    global LANGUAGE
    question, *options, correct_answer = question_set
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    if LANGUAGE == 'čeština':
        user_answer = input("Tvoje odpověd: ").strip().upper()
    else:
        user_answer = input("Your answer: ").strip().upper()

    return user_answer == correct_answer

def ask_name():
    """
    HG
    """
    global LANGUAGE
    if LANGUAGE == 'čeština':
        return input("Zadej svoje jméno: ").strip()
    else:
        return input("Enter your name: ").strip()

def millionaire(file_path):
    """
    GJ
    """
    global LANGUAGE
    name = ask_name()
    money = 0
    questions = load_questions(file_path)
    if LANGUAGE == 'čeština':
        print(f"Vítej, {name}!")
    else:
        print(f"Welcome, {name}!")
    print()

    for question_set in questions:
        if not question(question_set):
            print()
            if LANGUAGE == 'čeština':
                print("Špatně! Prohrál jsi.")
                print(f"Celkem máš peněz: ${money}")
            else:
                print("Incorrect! Game over.")
                print(f"Total money earned: ${money}")
            return

        print()
        if LANGUAGE == 'čeština':
            print("Šprávně! Získal jsi $1000.")
        else:
            print("Correct! You've earned $1000.")
        money += 1000
        if LANGUAGE == 'čeština':
            print(f"Celkem máš peněz: ${money}")
        else:
            print(f"Total money earned: ${money}")
        print()

if __name__ == "__main__":
    LANGUAGE = language_module.choose_language()
    if LANGUAGE == 'čeština':
        print(f"Pojď hrát milionáře v češtině.")
        millionaire("questions_cs.txt")
    else:
        print(f"Let's play Millionaire in {LANGUAGE}.")
        millionaire("questions_en.txt")

now = datetime.datetime.now()
print(now)
