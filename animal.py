from datetime import date

class Horse:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food
        self.walking = True
        self.date_added = date.today()

    def feed(self):
        return f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}'

    def __str__(self):
        return f'{self.name} is a {self.species}.'

class Dog:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food
        self.walking = True
        self.date_added = date.today()

    def feed(self):
        return f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}'

    def __str__(self):
        return f'{self.name} is a {self.species}.'

class Cat:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food
        self.walking = True
        self.date_added = date.today()

    def feed(self):
        return f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}'

    def __str__(self):
        return f'{self.name} is a {self.species}.'

class Squirrel:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food
        self.walking = True
        self.date_added = date.today()

    def feed(self):
        return f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}'

    def __str__(self):
        return f'{self.name} is a {self.species}.'        

class Groundhog:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food
        self.walking = True
        self.date_added = date.today()

    def feed(self):
        return f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}'

    def __str__(self):
        return f'{self.name} is a {self.species}.'        

class Duck:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.swimming = True
        self.date_added = date.today()

    def feed(self):
        return f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}'

    def __str__(self):
        return f'{self.name} is a {self.species}.'

class Flamingo:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.swimming = True
        self.date_added = date.today()

    def feed(self):
        return f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}'

    def __str__(self):
        return f'{self.name} is a {self.species}.'

class Goose:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.swimming = True
        self.date_added = date.today()

    def feed(self):
        return f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}'

    def __str__(self):
        return f'{self.name} is a {self.species}.'

class Loon:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.swimming = True
        self.date_added = date.today()

    def feed(self):
        return f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}'

    def __str__(self):
        return f'{self.name} is a {self.species}.'

class Goldfish:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.swimming = True
        self.date_added = date.today()

    def feed(self):
        return f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}'

    def __str__(self):
        return f'{self.name} is a {self.species}.'

class Snake:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.slithering = True
        self.date_added = date.today()

    def feed(self):
        return f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}'

    def __str__(self):
        return f'{self.name} is a {self.species}.'

class Lizard:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food
        self.walking = True
        self.date_added = date.today()

    def feed(self):
        return f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}'

    def __str__(self):
        return f'{self.name} is a {self.species}.'

class Spider:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food
        self.walking = True
        self.date_added = date.today()

    def feed(self):
        return f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}'

    def __str__(self):
        return f'{self.name} is a {self.species}.'

class Toad:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.hopping = True
        self.date_added = date.today()

    def feed(self):
        return f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}'

    def __str__(self):
        return f'{self.name} is a {self.species}.'

class Frog:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.hopping = True
        self.date_added = date.today()

    def feed(self):
        return f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}'

    def __str__(self):
        return f'{self.name} is a {self.species}.'

malcom = Frog('Malcom', 'Tree', 'crickets')
miles = Toad('Miles', 'Sonoran Desert', 'worms')
zane = Spider('Zane', 'Black Widow', 'morning', 'humans')
adrian = Lizard('Adrian', 'Chameleon', 'midday', 'maggots')
tom = Snake('Tom', 'Copperhead', 'mice')
leigha = Goldfish('Leigha', 'Gold Goldfish', 'fish food')
bryan = Loon('Bryan', 'Northern', 'cherrios')
joe = Goose('Joe', 'Canadian', 'minos')
sarah = Flamingo('Sarah', 'Purple', 'mosquitos')
luke = Duck('Luke', 'Mallard', 'bread')
eli = Groundhog('Eli', 'Nusance', 'afternoon', 'trash')
kaleb = Squirrel('Kaleb', 'Grey', 'morning', 'nuts')
michelle = Cat('Michelle', 'Mountain Lion', 'afternoon', 'sardines')
brian = Dog('Brian', 'Corgi', 'midday', 'wal-mart meat truck leftovers')
kirk = Horse('Kirk', 'Thoroughbred', 'morning', 'grains')

print(f'{kirk.name} the {kirk.species} is available to pet during the {kirk.shift} shift.')
print(kirk.feed())
print(kirk)
print(brian.feed())

