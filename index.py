from attractions import *
from animals import *

malcom = Frog('Malcom', 'Tree', 'crickets', 123454)
miles = Toad('Miles', 'Sonoran Desert', 'worms', 45678)
zane = Spider('Zane', 'Black Widow', 'humans', 4564)
adrian = Lizard('Adrian', 'Chameleon', 'maggots', 45678)
tom = Snake('Tom', 'Copperhead', 'mice', 4589897)
leigha = Goldfish('Leigha', 'Gold Goldfish', 'fish food', 21534)
bryan = Loon('Bryan', 'Northern', 'cherrios', 154684)
joe = Goose('Joe', 'Canadian', 'minos', 46848)
sarah = Flamingo('Sarah', 'Purple', 'mosquitos', 4846848)
luke = Duck('Luke', 'Mallard', 'bread', 48949)
eli = Groundhog('Eli', 'Nusance', 'afternoon', 'trash', 51684)
kaleb = Squirrel('Kaleb', 'Grey', 'morning', 'nuts', 156814894)
michelle = Cat('Michelle', 'Mountain Lion', 'afternoon', 'sardines', 18181)
brian = Dog('Brian', 'Corgi', 'midday', 'wal-mart meat truck leftovers', 1846)
kirk = Horse('Kirk', 'Thoroughbred', 'morning', 'grains', 12345)


print(kirk.chip_number)

kirk.chip_number = 57889

print(kirk.chip_number)
print(kirk.feed())
print(brian.feed())

varmint_village = PettingZoo('Varmint Village', 'cuddly critter gather here')
varmint_village.animals.extend([kirk, brian, michelle, kaleb, eli])
print(varmint_village)

for animal in varmint_village.animals:
    print(f'{animal.name} the {animal.species}')

slithering_sliders = SnakePit('Slithering Sliders', ' place where critters that are most likely not pettable gather here')
slithering_sliders.animals.extend([malcom, miles, zane, adrian, tom])
print(slithering_sliders)

for animal in slithering_sliders.animals:
    print(f'{animal.name} the {animal.species}')

dirty_pond = WetLands('Dirty Pond', 'critter of the that like to have bread thrown at them gather here')
dirty_pond.animals.extend([luke, sarah, joe, bryan, leigha])
print(dirty_pond)

for animal in dirty_pond.animals:
    print(f'{animal.name} the {animal.species}')


print(dirty_pond.last_critter_added)

bob = Goose('Bob', 'Swan', 'stale white bread', 546587)
bob.run()
bob.swim()
varmint_village.add_animal(bob)

for animal in varmint_village.animals:
    print(animal)

print(varmint_village)

karmen = Toad('Karmen', 'Giant Toad', 'worms', 454554)
varmint_village.add_animal(karmen)

