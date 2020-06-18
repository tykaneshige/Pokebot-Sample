from pokemon import *

class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon_caught = 0
        self.pokemon = {}
        self.pokemon_order = []

    # Function to catch Pokemon
    def add_pokemon(self, num, level, nickname=''):

        # Create a new pokemon object
        new_pokemon = Pokemon(num, level=level, nickname=nickname)

        # Add the pokemon to the list of pokemon owned by this trainer
        self.pokemon_order.append(len(self.pokemon))
        self.pokemon[len(self.pokemon)] = new_pokemon

        # Increment the number caught
        self.pokemon_caught += 1

    # Prints a list of Pokemon owned by this trainer
    def show_pokemon(self):

        # Check if the trainer has Pokemon
        if len(self.pokemon) == 0:
            print('You don\'t have any Pokemon!')
            return

        # Print the trainer's Pokemon in the order specified
        for num,key in enumerate(self.pokemon_order, start=1):
            if self.pokemon[key].nickname != '':
                print(str(num) + '. ' + self.pokemon[key].p_name + ', Nickname: \'' + self.pokemon[key].nickname + '\'') 
            else:
                print(str(num) + '. ' + self.pokemon[key].p_name) 

    # Function for returning trainer details
    def show_stats(self):
        print('Name: ' + str(self.name))
        print('No. Caught: ' + str(self.pokemon_caught))