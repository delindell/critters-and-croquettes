from .animal import Animal
from datetime import date
from movements import Walking

class Horse(Animal, Walking):

    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        self.shift = shift
        
    def feed(self):
        return f'{self.name} was fed {self.food} make sure he gets fed again at this time {date.today().strftime("%m/%d/%Y")}'
