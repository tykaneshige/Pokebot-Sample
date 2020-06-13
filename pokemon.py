from pokedex import *

class Pokemon:
    def __init__(self, num, level=1, nickname=''):
        self.id = num
        self.p_name = Pokedex[num]['Name']

        self.type = Pokedex[num]['Type']
        self.ability = Pokedex[num]['Ability']
        self.evolve_lv = Pokedex[num]['Evolve_Lv']
        self.evolve_to = Pokedex[num]['Evolve_To']

        # Optional Arguments
        self.level = level
        self.nickname = nickname

    # Prints data on the pokemon
    def pokedex_entry(self):
        print('Name: ' + self.p_name)

        if (self.nickname != ''):
            print('Nickname: ' + str(self.nickname))

        print('Level: ' + str(self.level))
        
        type_string = 'Type: '
        for types in self.type:
            type_string += types + ' '
        print(type_string)

        print('Ability: ' + self.ability)

        if (self.evolve_lv != -1):
            print('Evolves to ' + Pokedex[self.evolve_to]['Name'] + ' at level ' + str(self.evolve_lv) + '.')