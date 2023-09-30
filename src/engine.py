import numpy as np
from . import data

fields, questions = data.from_csv('data.csv')

# questions = {
#     1: 'yellow?',
#     2: 'bald?',
#     3: 'a man?',
#     4: 'short?',
# }

# characters = [
#     {'name': 'Homer Simpson',         'answers': {1: 1, 2: 1, 3: 1, 4: 0}},
#     {'name': 'SpongeBob SquarePants', 'answers': {1: 1, 2: 1, 3: 1, 4: 0.75}},
#     {'name': 'Sandy Cheeks',          'answers': {1: 0, 2: 0, 3: 0}},
# ]


def run():
    available_questions = set(questions.keys())
    questions_answered = []
    answers = []

    print("To jest proof of concept. Odpowiadaj liczbami w [0, 1]")

    while not stop_condition(available_questions):
        question_id = next_question(available_questions)
        questions_answered.append(question_id)
        answer = input(f"{questions[question_id]}: ")
        answers.append(float(answer))

        probs = calculate_probabilites(questions_so_far=questions, answers_so_far=answers)
        print(probs)

def stop_condition(questions):
    return len(questions) == 0

def next_question(available) -> int:
    return available.pop()

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

