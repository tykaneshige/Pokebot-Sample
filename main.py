# System packages
import random
import time

# User defined packages
from pokedex import *
from pokemon import *
from trainer import *

class Game:

    def __init__(self):
        self.trainers = {}
        self.current_trainer = ''
        self.pokemon = []
        self.pokemon_stats = {}

    # Create a new trainer
    def add_trainer(self):

        confirm = ''
        while confirm.lower() != 'y':

            name = input('Now tell me, what is your name? ')

            if name in self.trainers.keys():
                print('Sorry, that name is taken. Please choose another name.')
                continue

            if name.lower() == 'exit':
                return

            confirm = input('Ah, so your name is ' + str(name) + '? (Y/n) ')

            while 1:
                if confirm.lower() == 'y' or confirm.lower() == 'n':
                    break
                else:
                    confirm = input('Please enter Y or n. ')

        # Store trainer data
        new_trainer = Trainer(name)
        self.trainers[name] = new_trainer
        self.current_trainer = str(name)

        print('Very good ' + str(name) + '! Welcome to the wonderful world of Pokemon!\n')
    
    # Function for showing current trainer details
    def show_current(self):
        print('\nCurrent Trainer:')
        self.trainers[self.current_trainer].show_stats()
        print('\n')

    # Function for spawning pokemon
    def spawn_pokemon(self):

        # Randomly select the next pokemon 
        next_Pokemon = random.randint(1,3)

        # Verify that two of the same pokemon will not spawn at the same time
        first_Pokemon = next_Pokemon
        while next_Pokemon in self.pokemon:
            next_Pokemon += 1

            if next_Pokemon > HIGH_BOUND:
                next_Pokemon = 1

            if next_Pokemon == first_Pokemon:
                return

        # Add the pokemon to the list of available pokemon
        self.pokemon.append(next_Pokemon)

        # Randomly generate stats for the pokemon
        self.pokemon_stats[next_Pokemon] = {
            'Level': random.randint(1,99)
        }

        # Prompt user to name the pokemon
        print('Who\'s that Pokemon?')
        print(Pokedex[next_Pokemon]['Image_url'] + '\n')

    # Checks for a match from the available pokemon
    def match_pokemon(self, name):

        # Map the values of each available pokemon to their corresponding name
        poke_list = map((lambda num: Pokedex[num]['Name']), self.pokemon)

        # Search through the available pokemon list
        for i,p in enumerate(poke_list, start=0):
            if p.lower() == name.lower():
                print('Congratulations! You caught a level ' + str(self.pokemon_stats[self.pokemon[i]]['Level']) + ' ' + str(p) + '!\n')
                return

        # No available pokemon matched the response
        print('Try again.\n')
        return

    # See pokemon currently available to catch
    def show_pokemon(self):

        if len(self.pokemon) != 0:
            print('\nAvailable Pokemon:')
            print('Who\'s that Pokemon?')

            num = 1
            for p in self.pokemon:
                print(str(num) + '. ' + Pokedex[p]['Image_url'])
                num += 1
        else:
            print('\nThere are no Pokemon to catch. :(\n')

    # Main game loop
    def run(self):

        # Opening prompt from Professor Oak
        '''
        print('Hello there! Welcome to the world of Pokémon!')
        time.sleep(3)
        print('My name is Oak! People call me the Pokémon Prof!')
        time.sleep(3)
        print('This world is inhabited by creatures called Pokémon!')
        time.sleep(3)
        print('For some people, Pokémon are pets. Others use them for fights...')
        time.sleep(3)
        print('Your very own Pokémon adventure is about to unfold!')
        time.sleep(3)
        print('A world of dreams and adventures with Pokémon awaits! Let\'s go!')
        time.sleep(1)
        '''

        # Create a new trainer
        name = input('Now tell me, what is your name? ')

        confirm = ''
        while confirm.lower() != 'y':

            confirm = input('Ah, so your name is ' + str(name) + '? (Y/n) ')

            while 1:

                if confirm.lower() == 'y':
                    break
                elif confirm.lower() == 'n':
                    name = input('Ah, I see. So what is your name? ')
                    break
                else:
                    confirm = input('Please enter Y or n. ')

        new_trainer = Trainer(name)
        self.trainers[name] = new_trainer
        self.current_trainer = str(name)

        print('Very good ' + str(name) + '! It\'s time for you to dive into the world of Pokemon!\n')

        # Main loop of the game
        while 1:

            # Spawn pokemon after 10 inputs
            spawn_clock = 0
            while spawn_clock != 10:

                # Recieve and parse input from the user
                command = input()
                command_parse = command.split()

                # # Skip empty commands
                if len(command_parse) == 0:
                    continue

                # Check for a valid command
                if command_parse[0] == '!poke':

                    # Add a trainer
                    if len(command_parse) == 2 and command_parse[1].lower() == 'add':
                        self.add_trainer()

                    # Show current trainer
                    elif len(command_parse) == 2 and command_parse[1].lower() == 'current':
                        self.show_current()

                    # Guess a pokemon
                    elif len(command_parse) == 3 and command_parse[1].lower() == 'match':
                        self.match_pokemon(command_parse[2])

                    # Show available pokemon
                    elif len(command_parse) == 2 and command_parse[1].lower() == 'show':
                        self.show_pokemon()

                    # Exit the game
                    elif len(command_parse) == 2 and command_parse[1].lower() == 'exit':
                        return

                    else:
                        print('\nInvalid command. See \'!poke help\' for more information.\n')
                else:
                    spawn_clock += 1

            self.spawn_pokemon()

game = Game()
game.run()