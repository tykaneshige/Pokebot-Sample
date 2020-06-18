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
!poke add
-This command creates a new trainer.

!poke remove
-This command removes a trainer.
-The trainer you are currently using cannot be removed.

!poke switch
-This command switches to another trainer.

!poke current
-This command shows some stats on the trainer you are currently using.

!poke list
-This command shows the pokemon currently owned by the trainer.

!poke catch <pokemon>
-This command attempts to catch a pokemon.
-If the name matches a pokemon that is currently spawned in, the trainer will catch it.

!poke show
-This command shows all image urls of spawned-in pokemon.

!poke exit
-This command exits the program.
```
