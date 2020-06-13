from pokemon import *

class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon_caught = 0
        self.pokemon = {}
        self.next_key = 0

    # Function to catch Pokemon
    def catch_Pokemon(self, num, level, nickname=''):

        # Create a new pokemon object
        new_Pokemon = Pokemon(num, level=level, nickname=nickname)

        # Add the pokemon to the list of pokemon owned by this trainer
        self.pokemon[next_key] = new_Pokemon
        self.pokemon_caught += 1

        # Increment the key
        next_key += 1
    
    # Function for returning trainer details
    def show_stats(self):
        print('Name: ' + str(self.name))
        print('No. Caught: ' + str(self.pokemon_caught))