import csv

def parse_percent(s):
    return float(s.replace("%", "")) / 100

def from_csv(file):
    data = {}
    with open(file) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        header = next(spamreader)
        categories = list(header)[1:]
        print(categories)
        for row in spamreader:
            key = row[0]
            vals = list(map(parse_percent, row[1:]))
            print(vals)



    exit(1)
    return data
