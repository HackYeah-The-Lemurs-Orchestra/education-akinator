import numpy as np
# from pprint import pprint

def calculate_probabilites(questions_so_far, answers_so_far):
    probabilities = []
    for character in characters:
        probabilities.append({
            'name': character['name'],
            'probability': calculate_character_probability(character, questions_so_far, answers_so_far)
        })

    return probabilities

def calculate_character_probability(character, questions_so_far, answers_so_far):
    # Prior
    P_character = 1 / len(characters)

    # Likelihood
    P_answers_given_character = 1
    P_answers_given_not_character = 1
    for question, answer in zip(questions_so_far, answers_so_far):
        P_answers_given_character *= max(
            1 - abs(answer - character_answer(character, question)), 0.01)

        P_answer_not_character = np.mean([1 - abs(answer - character_answer(not_character, question))
                                          for not_character in characters
                                          if not_character['name'] != character['name']])
        P_answers_given_not_character *= max(P_answer_not_character, 0.01)

    # Evidence
    P_answers = P_character * P_answers_given_character + \
        (1 - P_character) * P_answers_given_not_character

    # Bayes Theorem
    P_character_given_answers = (
        P_answers_given_character * P_character) / P_answers

    return P_character_given_answers


def character_answer(character, question):
    if question in character['answers']:
        return character['answers'][question]
    return 0.5

questions = {
    1: 'yellow?',
    2: 'bald?',
    3: 'a man?',
    4: 'short?',
}

characters = [
    {'name': 'Homer Simpson',         'answers': {1: 1, 2: 1, 3: 1, 4: 0}},
    {'name': 'SpongeBob SquarePants', 'answers': {1: 1, 2: 1, 3: 1, 4: 0.75}},
    {'name': 'Sandy Cheeks',          'answers': {1: 0, 2: 0, 3: 0}},
]

def main():
    questions_so_far = [2]
    answers_so_far = [0.75]

    probabilities = calculate_probabilites(questions_so_far, answers_so_far)
    print("probabilities", probabilities)


if __name__ == "__main__":
    main()