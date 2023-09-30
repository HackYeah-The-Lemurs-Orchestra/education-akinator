
class StudyAttribute(object):
    def __init__(self, name):
        self.name = name


class University(object):
    def __init__(self, name):
        self.name = name


Scisle = StudyAttribute("Ścisłe")
Zdrowie = StudyAttribute("Zdrowie")
Medyczne = StudyAttribute("Medyczne")
IT = StudyAttribute("IT")
Chemia = StudyAttribute("Chemia")
Zarzadzanie = StudyAttribute('Zarzadzanie')
Filologia = StudyAttribute('Filologia')
Matematyka = StudyAttribute('Matematyka')
Prawo = StudyAttribute('Prawo')
Rozrywka = StudyAttribute('Rozrywka')
Categories = [Scisle, Zdrowie, Medyczne, IT, Chemia, Zarzadzanie, Filologia, Matematyka, Prawo]

UJ = University("UJ")
AGH = University("AGH")


class Study(object):
    def __init__(self, name, university, categories, part_time=False, degree=1):
        self.name = name
        self.university = university
        self.categories = categories,
        # stacjonarne:
        self.part_time = part_time
        # stopien:
        self.degree = degree


db_studies = list()
db_studies.append(Study(name='Informatyka', university=UJ,
                        categories={
                            Matematyka: 0.9,
                            Scisle: 1,
                            IT: 1
                        }))
db_studies.append(Study(name='Informatyka gier komputerowa', university=UJ,
                        categories={
                            Matematyka: 0.9,
                            Scisle: 1,
                            IT: 1,
                            Rozrywka: 0.9
                        }))

db_studies.append(Study(name='Dietetyka', university=UJ,
                        categories={
                            Zdrowie: 1,
                            Chemia: 0.5,
                            Medyczne: 0.4
                        }))

db_studies.append(Study(name="Położnictwo", university='UJ',
                        categories={
                            Zdrowie: 1,
                            Medyczne: 0.9
                        }))
