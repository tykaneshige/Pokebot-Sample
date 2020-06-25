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
    def add_trainer(self, name):

        # Verify that two trainers do not share the same name
        if name in self.trainers.keys():
            print('Sorry, that name is taken. Please choose another name.\n')
            return

        # Continue to prompt the user for input until a valid name is passed
        confirm = ''
        while 1:

            confirm = input('Would you like to add trainer \'' + str(name) + '\'? (Y/n) ')

            if confirm.lower() == 'y':
                break
            elif confirm.lower() == 'n':
                print('Exiting trainer add.\n')
                return
            else:
                print('Please enter Y or n.')

        # Store trainer data
        new_trainer = Trainer(name)
        self.trainers[name] = new_trainer

        print('Very good ' + str(name) + '! Welcome to the wonderful world of Pokemon!\n')

    # Function for removing trainers
    def remove_trainer(self, name):

        # You cannot remove the trainer you are current playing as
        if name == self.current_trainer:
            print('You cannot delete the trainer you are currently using!\n')
            return

        # Verify that the trainer exists
        if name not in self.trainers:
            print('Trainer not found.\n')
            return

        # Prompt the user for input and remove the trainer
        while 1:

            # Prompt the user for confirmation
            confirm = input('Are you sure you would like to remove trainer \'' + str(name) + '\'? This action cannot be undone. (Yes/No) ')

            if confirm.lower() == 'yes':
                print('Deleting trainer \'' + str(name) + '\'...')
                self.trainers.pop(name, None)
                time.sleep(2)
                print('Trainer deleted.\n')
                return
            elif confirm.lower() == 'no':
                print('Exiting trainer removal.\n')
                return
            else:
                print('Please enter \'Yes\' or \'no\'.')

    # Function for switching between trainers
    def switch_trainer(self, name):

        # Verify that the trainer exists
        if name not in self.trainers:
            print('Trainer not found.\n')
            return

        # Verify that there are other trainers to remove
        if name == self.current_trainer:
            print('You are current playing as that trainer!\n')
        else:
            print('Successively switched to trainer \'' + str(name) + '\'.\n')
            self.current_trainer = str(name)

    # Function for showing current trainer details
    def show_current(self):

        # Print the current trainer
        print('\nCurrent Trainer:')
        self.trainers[self.current_trainer].show_stats()

        # Print other available trainers
        if len(self.trainers) > 1:
            print('\nAvailable Trainers:')
            for key, value in self.trainers.items():
                if key != self.current_trainer:
                    print(key)

        print()   # Adds a newline - print() will add a newline by default

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

    # Function for despawning pokemon
    def despawn_pokemon(self, key):

        # Verify the key exists
        if key in self.pokemon:
            self.pokemon.pop(key)

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
                        nickname = ''
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

                # Despawn pokemon
                self.despawn_pokemon(key)

                return

        # No available pokemon matched the response
        print('Try again.\n')
        return
    
    # Function for releasing Pokemon
    def release_pokemon(self, index):

        trainer = self.trainers[self.current_trainer]
        num = int(index) - 1

        # Check if the current trainer has Pokemon
        if len(trainer.pokemon) == 0:
            print('You don\'t have any Pokemon!\n')
            return

        # Check for valid indicies
        if num < 0 or num >= len(trainer.pokemon):
            print('Invalid index.\n')
            return

        key = trainer.pokemon_order[num]
        pokemon = trainer.pokemon[key]

        # Prompt confirmation from the trainer
        while 1:

            if pokemon.nickname == '':
                confirm = input('Are you sure you would like to release ' + pokemon.p_name + '? This action cannot be undone. (Yes/no) ')
            else:
                confirm = input('Are you sure you would like to release ' + pokemon.nickname + '? This action cannot be undone. (Yes/no) ')

            if confirm.lower() == 'yes':
                break
            elif confirm.lower() == 'no':
                print('Exiting pokemon release.\n')
                return
            else:
                print('Please enter \'Yes\' or \'no\'.')

        # Remove the pokemon from the trainer
        if pokemon.nickname == '':
            print('Bye bye ' + pokemon.p_name + '!\n')
        else:
            print('Bye bye ' + pokemon.nickname + '!\n')

        trainer.remove_pokemon(key)

    # List Pokemon owned by the current trainer
    def list_pokemon(self):
        
        trainer = self.trainers[self.current_trainer]

        # Check if the trainer has Pokemon
        if len(trainer.pokemon) == 0:
            print('You don\'t have any Pokemon!\n')
        else:
            trainer.show_pokemon()
            print()

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

    # Function for printing the help message
    def show_help(self):

        print('All commands are be prefixed with \'!poke\'.')
        print('\'add <trainer_name>\' - Creates a new trainer.')
        print('\'remove <trainer_name>\' - Removes a trainer.')
        print('\'switch <trainer_name>\' - Switches to another trainer.')
        print('\'current\' - Shows details on the current trainer.')
        print('\'catch <pokemon_name>\' - Attempts to catch a pokemon.')
        print('\'release <list_num>\' - Releases a pokemon.')
        print('\'list\' - Lists the pokemon owned by the current trainer.')
        print('\'show\' - Lists the pokemon currently spawned.')
        print('\'exit\' - Exits the program.\n')

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
        time.sleep(3)

        # Continually prompt the user for a name
        name = input('Now tell me, what is your name? ')

        confirm = ''
        while confirm.lower() != 'y':

            confirm = input('Ah, so your name is ' + str(name) + '? (Y/n) ')

            while 1:
                if confirm.lower() == 'y':
                    break
                elif confirm.lower() == 'n':
                    name = input('Oh, I see. So what is your name? ')
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
                    if len(command_parse) == 3 and command_parse[1].lower() == 'add':
                        self.add_trainer(command_parse[2])

                    # Remove a trainer
                    elif len(command_parse) == 3 and command_parse[1].lower() == 'remove':
                        self.remove_trainer(command_parse[2])

                    # Switch to a different trainer
                    elif len(command_parse) == 3 and command_parse[1].lower() == 'switch':
                        self.switch_trainer(command_parse[2])

                    # Show current trainer
                    elif len(command_parse) == 2 and command_parse[1].lower() == 'current':
                        self.show_current()

                    # List currently owned Pokemon
                    elif len(command_parse) == 2 and command_parse[1].lower() == 'list':
                        self.list_pokemon()

                    # Guess a pokemon
                    elif len(command_parse) == 3 and command_parse[1].lower() == 'catch':
                        self.catch_pokemon(command_parse[2])

                    # Release pokemon
                    elif len(command_parse) == 3 and command_parse[1].lower() == 'release':
                        self.release_pokemon(command_parse[2])
 
                    # Show available Pokemon
                    elif len(command_parse) == 2 and command_parse[1].lower() == 'show':
                        self.show_pokemon()

                    # Displays a help message
                    elif len(command_parse) == 2 and command_parse[1].lower() == 'help':
                        self.show_help()

                    # Exit the game
                    elif len(command_parse) == 2 and command_parse[1].lower() == 'exit':
                        print('Thanks for playing!')
                        return

                    # Invalid command
                    else:
                        print('Command: ' + str(command))
                        print('\nInvalid command. See \'!poke help\' for more information.\n')

                else:
                    spawn_clock += 1

            self.spawn_pokemon()

# Main function
if __name__ == '__main__':
    game = Game()
    game.run()