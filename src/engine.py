import numpy as np
import math
import copy
from functools import cmp_to_key
from . import data
import os

fields, questions = data.from_csv('data.csv')
questions = {
    0: "Lubię matematykę",
    1: "Chciałbym pracować na zewnątrz",
    2: "Chciałbym zajmować się sprzedażą",
    3: "Lubię pracować w zespole",
    4: "Moim celem jest pomoc środowisku",
    5: "Lubię łamigłówki",
    6: "Jestem bardzo kreatywny",
    7: "Dobrze się bawię podejmując ryzyko",
    8: "Moim hobby jest rysowanie",
    9: "Fascynuje mnie historia"
}

def run():
    available_questions = set(questions.keys())
    questions_answered = []
    answers = []
    probs = None

    while not stop_condition(available_questions):
        question_id = next_question(questions_answered, answers, available_questions)
        questions_answered.append(question_id)
        print(f"{questions[question_id]}: ")
        answer = menu() # input(f"{questions[question_id]}: ")
        answers.append(float(answer))

        probs = calculate_probabilites(questions_so_far=questions_answered, answers_so_far=answers)
        os.system("clear")

    top(sorted(probs, key=cmp_to_key(compare), reverse=True))

def top(fields):
    print("-----Polecane kierunki-----")
    for i in range(5):
        print(f"kierunek: {fields[i]['name']} Stopien dopasowania: {int(fields[i]['probability']*100)}%")


def menu():
    print("1. Tak")
    print("2. Chyba tak")
    print("3. Nie wiem")
    print("4. Chyba nie")
    print("5. Nie")
    answer = int(input("Odpowiedz: "))
    p = 0
    match answer:
        case 1:
            p = 1
        case 2:
            p = 0.75
        case 3:
            p = 0.5
        case 4:
            p = 0.25
        case 5:
            p = 0
    return p

def compare(item1, item2):
    if item1['probability'] < item2['probability']:
        return -1
    elif item1['probability'] > item2['probability']:
        return 1
    else:
        return 0


def stop_condition(questions):
    return len(questions) == 0


def next_question(questions_so_far, answers_so_far, quezdionz) -> int:
    next_entropies = []
    for quezdion in quezdionz:
        new_questions = copy.deepcopy(questions_so_far)
        new_questions.append(quezdion)
        new_answers = copy.deepcopy(answers_so_far)
        new_answers.append(1)
        next_probabilities = calculate_probabilites(new_questions, new_answers)
        next_entropies.append((entropy(next_probabilities), quezdion))
    min_entropy = next_entropies[0][0]
    question = next_entropies[0][1]
    for etr in next_entropies:
        if etr[0] < min_entropy:
            min_entropy = etr[0]
            question = etr[1]

    quezdionz.remove(question)

    return question


def entropy(probabilities):
    e = 0
    for pi in probabilities:
        e += -pi['probability'] * math.log(pi['probability'], 2)

    return e


def calculate_probabilites(questions_so_far, answers_so_far):
    probabilities = []
    for field in fields:
        probabilities.append({
            'name': field['name'],
            'probability': calculate_field_probability(field, questions_so_far, answers_so_far)
        })

    return probabilities


def calculate_field_probability(field, questions_so_far, answers_so_far):
    # Prior
    P_character = 1 / len(fields)

    # Likelihood
    P_answers_given_character = 1
    P_answers_given_not_character = 1
    for question, answer in zip(questions_so_far, answers_so_far):
        P_answers_given_character *= max(
            1 - abs(answer - field_answer(field, question)), 0.01)

        probs = [1 - abs(answer - field_answer(not_field, question))
                 for not_field in fields
                 if not_field['name'] != field['name']]
        P_answer_not_character = np.mean(probs)
        P_answers_given_not_character *= max(P_answer_not_character, 0.01)

    # Evidence
    P_answers = P_character * P_answers_given_character + \
                (1 - P_character) * P_answers_given_not_character

    # Bayes Theorem
    P_character_given_answers = (
                                        P_answers_given_character * P_character) / P_answers

    return P_character_given_answers


def field_answer(field, question):
    if question in field['answers']:
        return field['answers'][question]
    return 0.5
