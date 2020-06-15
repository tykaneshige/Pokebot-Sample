from pokemon import *

class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon_caught = 0
        self.pokemon = {}

    # Function to catch Pokemon
    def catch_Pokemon(self, num, level, nickname=''):

        # Create a new pokemon object
        new_Pokemon = Pokemon(num, level=level, nickname=nickname)

        # Add the pokemon to the list of pokemon owned by this trainer
        self.pokemon[len(pokemon)] = new_Pokemon

        # Increment the key
        next_key += 1
    
    # Function for returning trainer details
    def show_stats(self):
        print('Name: ' + str(self.name))
        print('No. Caught: ' + str(self.pokemon_caught))