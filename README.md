# Pokebot-Sample
Sample program for the Pokebot implementation (non-server implementation).

---

## Instructions
* Clone or download the repository off of Github.
* Run the following command to start the program:

```
python main.py
```

* If the above command does not work, download python 3.8 and try the following command:

```
python3 main.py
```

---

## Some Commands

* All valid commands to the program will be prefixed with '!poke'. 
* Some commands are listed below:

```
!poke add <trainer_name>
-This command creates a new trainer.
-This command does not automatically switch trainers.

!poke remove <trainer_name>
-This command removes a trainer.
-The trainer you are currently using cannot be removed.

!poke switch <trainer_name>
-This command switches to another trainer.

!poke current
-This command shows some stats on the trainer you are currently using.
-This command also lists other available trainers.

!poke catch <pokemon>
-This command attempts to catch a pokemon.
-If the name matches a pokemon that is currently spawned in, the trainer will catch it.

!poke release <list_num>
-This command releases a pokemon owned by the current trainer.
-<list_num> is the number of the pokemon as seen from the command "!poke list"

!poke list
-This command shows the pokemon currently owned by the trainer.

!poke show
-This command shows all image urls of spawned-in pokemon.

!poke exit
-This command exits the program.
```

---

## Not Implemented
* Pokemon do not despawn after a given amount of time.
* There is no functionality for ordering a trainer's Pokemon.
* No command exists to get data on a certain Pokemon.