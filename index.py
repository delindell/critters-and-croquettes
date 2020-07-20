from attractions import *
from animals import *

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

varmint_village = PettingZoo('Varmint Village')
varmint_village.animals.extend([kirk, brian, michelle, kaleb, eli])
print(varmint_village)

for animal in varmint_village.animals:
    print(f'{animal.name} the {animal.species}')

slithering_sliders = SnakePit('Slithering Sliders')
slithering_sliders.animals.extend([malcom, miles, zane, adrian, tom])
print(slithering_sliders)

for animal in slithering_sliders.animals:
    print(f'{animal.name} the {animal.species}')

dirty_pond = WetLands('Dirty Pond')
dirty_pond.animals.extend([luke, sarah, joe, bryan, leigha])
print(dirty_pond)

for animal in dirty_pond.animals:
    print(f'{animal.name} the {animal.species}')

