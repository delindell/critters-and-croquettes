from .attraction import Attraction

class PettingZoo(Attraction):

    def __init__(self, name, description):
        super().__init__(name, description)

    def add_animal(self, animal):
        try:
            if animal.walk_speed >= 0:
                self.animals.append(animal)
        except AttributeError:
            print(f'{animal} and does not belong here')
