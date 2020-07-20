class PettingZoo:

    def __init__(self, name):
        self.attraction_name = name
        self.description = 'place where cuddly creatures congrigate like'
        self.animals = []

    # getter
    @property
    def last_critter_added(self):
        return f'{self.animals[-1].name} the {self.animals[-1].species}'

    def __str__(self):
        return f'{self.attraction_name} is a {self.description}'

class SnakePit:

    def __init__(self, name):
        self.attraction_name = name
        self.description = 'place where dangerous creatures congrigate like'
        self.animals = []

    # getter
    @property
    def last_critter_added(self):
        return f'{self.animals[-1].name} the {self.animals[-1].species}'

    def __str__(self):
        return f'{self.attraction_name} is a {self.description}'
        

class WetLands:
    
    def __init__(self, name):
        self.attraction_name = name
        self.description = 'place where creatures that enjoy water in some capacity live like'
        self.animals = []

    # getter
    @property
    def last_critter_added(self):
        return f'{self.animals[-1].name} the {self.animals[-1].species}'


    def __str__(self):
        return f'{self.attraction_name} is a {self.description}'
