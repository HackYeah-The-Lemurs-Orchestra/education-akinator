import csv

fields = [
    {'name': 'Matematyka stosowana', 'answers': {1: 1, 2: 0.5}},
    {'name': 'Informatyka',          'answers': {1: 0.8, 2: 1}},
]

def parse_percent(s):
    return float(s.replace("%", "")) / 100

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
