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
        self.pokemon = {}

    # Function for creating a new trainer
    def add_trainer(self):

        # Continue to prompt the user for input until a valid name is passed
        confirm = ''
        while confirm.lower() != 'y':

            name = input('What is your name? Enter \'exit\' to cancel trainer add. ')

            if name.lower() == 'exit':
                print()
                return

            if name in self.trainers.keys():
                print('Sorry, that name is taken. Please choose another name.')
                continue

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

    # Function for removing trainers
    def remove_trainer(self):

        # Verify that there are other trainers to remove
        # You cannot remove the trainer you are current playing as
        if len(self.trainers) == 1:
            print('You cannot delete the trainer you are currently using!\n')
            return

        # Prompt the user for input and remove the trainer
        while 1:

            print('Please enter the name of the trainer you would like to remove.')
            print('Enter \'list\' to print a list of trainers.')
            remove = input('Enter \'exit\' to cancel trainer removal. ')

            if remove == '':
                print('\nPlease enter a value.')
                continue

            if remove.lower() == 'exit':
                return

            if remove.lower() == 'list':
                self.print_trainers()
                continue

            # Verify that the trainer exists
            if remove not in self.trainers:
                print('Trainer not found.')
                continue
            else:
                # Prompt the user for confirmation
                confirm = input('\nAre you sure you would like to remove trainer \'' + str(remove) + '\'? This action cannot be undone. (Yes/No) ')

                if confirm.lower() == 'yes':
                    print('Deleting trainer \'' + str(remove) + '\'...')
                    self.trainers.pop(remove, None)
                    time.sleep(2)
                    print('Trainer deleted.\n')
                    return
                else:
                    break

    # Function for switching between trainers
    def switch_trainer(self):

        # Verify that there are other trainers to remove
        if len(self.trainers) == 1:
            print('There are no trainers to switch to.\n')
            return

        # Prompt the user for input and switch to the trainer
        while 1:

            print('Please enter the name of the trainer you would like to switch to.')
            print('Enter \'list\' to print a list of trainers.')
            switch = input('Enter \'exit\' to cancel trainer switch. ')

            if switch == '':
                print('Please enter a value.')
                continue

            if switch.lower() == 'exit':
                return

            if switch.lower() == 'list':
                self.print_trainers()
                continue

            # Verify that the trainer exists
            if switch not in self.trainers:
                print('Trainer not found.')
                continue
            else:
                print('Successively switched to trainer \'' + str(switch) + '\'.\n')
                self.current_trainer = str(switch)
                break

    # Function for showing current trainer details
    def show_current(self):
        print('\nCurrent Trainer:')
        self.trainers[self.current_trainer].show_stats()
        print()   # Adds a newline - print() will add a newline by default

    # Function for printing a list of available trainers
    def print_trainers(self):
        print('\nAvailable Trainers:')
        for key, value in self.trainers.items():
            if key != self.current_trainer:
                print(key)

    # Function for spawning pokemon
    def spawn_pokemon(self):

        # Only 5 Pokemon may spawn in at a time
        if len(self.pokemon) == 5:
            return

        # Randomly select the next pokemon 
        next_pokemon = random.randint(LOW_BOUND, HIGH_BOUND)

        # Verify that two of the same Pokemon will not spawn at the same time
        while next_pokemon in self.pokemon:
            next_pokemon = random.randint(LOW_BOUND, HIGH_BOUND)

        # Randomly generate stats for the pokemon
        new_pokemon = {
            'Name': Pokedex[next_pokemon]['Name'],
            'Level': random.randint(1,99),
            'URL': Pokedex[next_pokemon]['Image_url']
        }

        # Add the pokemon to the list of available Pokemon
        self.pokemon[next_pokemon] = new_pokemon

        # Prompt user to name the pokemon
        print('\nWho\'s that Pokemon?')
        print(new_pokemon['URL'] + '\n')

    # Function for matching user input with available Pokemon
    def catch_pokemon(self, name):

        # Verify that there are Pokemon to catch
        if len(self.pokemon) == 0:
            print('There are no Pokemon to catch!\n')
            return

        # Search through the available pokemon list
        for key,p in self.pokemon.items():
            if p['Name'].lower() == name.lower():
                print('Congratulations! You caught a level ' + str(p['Level']) + ' ' + p['Name'] + '!\n')

                # Prompt user for a nickname
                while 1:

                    confirm = input('Would you like give your caught ' + p['Name'] + ' a nickname? (Y/n) ')

                    if confirm.lower() != 'y' and confirm.lower() != 'n':
                        print('Please enter \'Y\' or \'n\'.')
                        continue
                    elif confirm.lower() == 'n':
                        break;
                    else:
                        nickname = input('What should its nickname be? ')
                        break;

                # Add the Pokemon to the trainer who caught it
                self.trainers[self.current_trainer].add_pokemon(
                    key,
                    p['Level'],
                    nickname=nickname)

                if nickname != '':
                    print('Successfully stored ' + str(nickname) + '.\n')
                else:
                    print('Successfully stored ' + p['Name'] + '.\n')

                return

        # No available pokemon matched the response
        print('Try again.\n')
        return

    # Function for listing currently available Pokemon
    def show_pokemon(self):

        # Verify that there are Pokemon available
        if len(self.pokemon) != 0:

            print('Who\'s that Pokemon?')

            for val,(num,p) in enumerate(self.pokemon.items(), start=1):
                print(str(val) + '. ' + p['URL'])
            print()

        else:
            print('There are no Pokemon to catch. :(\n')

    # List Pokemon owned by the current trainer
    def list_pokemon(self):
        self.trainers[self.current_trainer].show_pokemon()
        print()

    # Main game loop
    def run(self):

        # Opening prompt from Professor Oak
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
        print('A world of dreams and adventures with Pokémon awaits! Let\'s go!\n')
        time.sleep(1)

        # Continually prompt the user for a name
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

        # Create a new trainer
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

                # # Skip empty inputs
                if len(command_parse) == 0:
                    continue

                # Check for a valid command
                if command_parse[0] == '!poke':

                    # Add a trainer
                    if len(command_parse) == 2 and command_parse[1].lower() == 'add':
                        self.add_trainer()

                    # Remove a trainer
                    elif len(command_parse) == 2 and command_parse[1].lower() == 'remove':
                        self.remove_trainer()

                    # Switch to a different trainer
                    elif len(command_parse) == 2 and command_parse[1].lower() == 'switch':
                        self.switch_trainer()

                    # Show current trainer
                    elif len(command_parse) == 2 and command_parse[1].lower() == 'current':
                        self.show_current()

                    # Guess a pokemon
                    elif len(command_parse) == 3 and command_parse[1].lower() == 'catch':
                        self.catch_pokemon(command_parse[2])

                    # Show available Pokemon
                    elif len(command_parse) == 2 and command_parse[1].lower() == 'show':
                        self.show_pokemon()

                    # List currently owned Pokemon
                    elif len(command_parse) == 2 and command_parse[1].lower() == 'list':
                        self.list_pokemon()

                    # Exit the game
                    elif len(command_parse) == 2 and command_parse[1].lower() == 'exit':
                        return

                    # Invalid command
                    else:
                        print('Command: ' + str(command))
                        print('\nInvalid command. See \'!poke help\' for more information.\n')

                else:
                    spawn_clock += 1

            self.spawn_pokemon()

game = Game()
game.run()