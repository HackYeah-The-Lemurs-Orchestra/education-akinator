import csv

def parse_percent(s):
    return float(s.replace("%", "")) / 100

# returns
# fields = [
#     {'name': 'Homer Simpson',         'answers': {1: 1, 2: 1, 3: 1, 4: 0}},
#     {'name': 'SpongeBob SquarePants', 'answers': {1: 1, 2: 1, 3: 1, 4: 0.75}},
#     {'name': 'Sandy Cheeks',          'answers': {1: 0, 2: 0, 3: 0}},
# ]

# questions = {
#     1: 'yellow?',
#     2: 'bald?',
#     3: 'a man?',
#     4: 'short?',
# }

def from_csv(file):
    questions = {}
    fields = []
    with open(file) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        header = next(spamreader)
        questions = dict(enumerate(list(header)[1:]))
        print(questions)

        for row in spamreader:
            field = row[0]
            vals = dict(zip(questions,
                        map(parse_percent, row[1:]))
                    )
            fields.append({
                "name": field,
                "answers": vals
            })

    return fields, questions
