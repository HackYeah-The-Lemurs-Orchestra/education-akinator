import numpy as np
import math
import copy
from functools import cmp_to_key
from . import data

fields, questions = data.from_csv('data.csv')

def run():
    available_questions = set(questions.keys())
    questions_answered = []
    answers = []

    print("To jest proof of concept. Odpowiadaj liczbami w [0, 1]")

    while not stop_condition(available_questions):
        question_id = next_question(questions_answered, answers, available_questions)
        questions_answered.append(question_id)
        answer = input(f"{questions[question_id]}: ")
        answers.append(float(answer))

        probs = calculate_probabilites(questions_so_far=questions, answers_so_far=answers)
        print(sorted(probs, key=cmp_to_key(compare)))

def compare(item1, item2):
    if item1['probability'] > item2['probability']:
        return -1
    elif item1['probability'] < item2['probability']:
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
        e += pi['probability'] * math.log(pi['probability'], 2)

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

        P_answer_not_character = np.mean([1 - abs(answer - field_answer(not_field, question))
                                          for not_field in fields
                                          if not_field['name'] != field['name']])
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

