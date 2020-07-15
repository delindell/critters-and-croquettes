from datetime import date

class Horse:

    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.walking = True
        self.date_added = date.today()

class Dog:

    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.walking = True
        self.date_added = date.today()

class Cat:

    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.walking = True
        self.date_added = date.today()

class Squirrel:

    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.walking = True
        self.date_added = date.today()

class Groundhog:

    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.walking = True
        self.date_added = date.today()

class Duck:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()

class Flamingo:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()

class Goose:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()

class Loon:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()

class Goldfish:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()

class Snake:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()

class Lizard:

    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.walking = True
        self.date_added = date.today()

class Spider:

    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.shift = shift
        self.walking = True
        self.date_added = date.today()

class Toad:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.hopping = True
        self.date_added = date.today()

class Frog:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.hopping = True
        self.date_added = date.today()

malcom = Frog('Malcom', 'Tree')
miles = Toad('Miles', 'Sonoran Desert')
zane = Spider('Zane', 'Black Widow', 'morning')
adrian = Lizard('Adrian', 'Chameleon', 'midday')
tom = Snake('Tom', 'Copperhead')
leigha = Goldfish('Leigha', 'Gold Goldfish')
bryan = Loon('Bryan', 'Northern')
joe = Goose('Joe', 'Canadian')
sarah = Flamingo('Sarah', 'Purple')
luke = Duck('Luke', 'Mallard')
eli = Groundhog('Eli', 'Nusance', 'afternoon')
kaleb = Squirrel('Kaleb', 'Grey', 'morning')
michelle = Cat('Michelle', 'Mountain Lion', 'afternoon')
brian = Dog('Brian', 'Corgi', 'midday')
kirk = Horse('Kirk', 'Thoroughbred', 'morning')

print(f'{kirk.name} the {kirk.species} is available to pet during the {kirk.shift} shift.')
