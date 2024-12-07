import numpy as np 
import random
from icecream import ic


def monty_hall_simulation_ai(n=1000, switch=True):
    # Anzahl der Gewinne
    wins = 0
    # Anzahl der Türen
    doors = [0, 1, 2]
    for _ in range(n):
        # Auto hinter einer der Türen
        car = np.random.randint(0, 3)
        # Spieler wählt eine Tür
        choice = np.random.randint(0, 3)
        # Monty öffnet eine der verbleibenden Türen
        open_door = np.random.choice([door for door in doors if door != choice and door != car])
        # Spieler wechselt die Tür
        if switch:
            choice = [door for door in doors if door != choice and door != open_door][0]
        # Überprüfen, ob der Spieler gewonnen hat
        if choice == car:
            wins += 1
    return wins / n

def mh_sim_sr(choice:int, doors:list)-> bool:
    """
    Monty Hall Simulation
    Params:
    choice: int - the door the player chooses
    doors: list - the doors available (col1) and the car location (col2)
    Returns:
    bool - True, if the player wins
    """
    nr_doors = len(doors)
    assert choice < nr_doors, "Invalid choice"
    assert sum(doors) == 1, "There must be exactly one car"
    
    # Doors count 1 to nr_doors, arrays count 0 to nr_doors-1
    choice -= 1
    
    # Monty opens a random door (not the player's choice and not the car)
    other = random.choice([door for door in range(nr_doors) if door != choice and not doors[door]])
    
    # Player switches to the other door
    # ic("Monty opens door", other+1) 
    
    # Player switches to the other door?
    if random.random() > 0.5:
        # ic("Player changes the door")
        new_choice = random.choice([door for door in range(nr_doors) if door != choice and door != other])
    else:
        # ic("Player keeps the door")
        new_choice = choice 
       
    # Player wins if the car is behind the chosen door
    return doors[new_choice], new_choice != choice

    
def shuffle_doors(n_doors:int = 3) -> list:
    doors = [False for _ in range(n_doors)]
    doors[random.randint(0, n_doors-1)] = True
    return doors
    
if __name__ == "__main__":
    n_doors = 3
    n_runs = 300000
    
    # result, change = mh_sim_sr(choice, doors)
    win_keep = win_change = loose_keep = loose_change = 0
    for _ in range(n_runs):
        doors = shuffle_doors(n_doors)
        choice = random.randint(0, n_doors-1)
        win,  switch = mh_sim_sr(choice, doors)
        # print(f'Player {["looses", "wins"][result[0]]}\tby '
        #      f'{"changing" if result[1] else "keeping"} the door')
        if win:
            if switch:
                win_change += 1
            else:
                win_keep += 1
        else:
            if switch:
                loose_change += 1
            else:
                loose_keep += 1
    
    print(f'Wins by changing: {win_change}\tWins by keeping: {win_keep}')
    print(f'Ratio: {win_change / win_keep:.2f}') if win_keep > 0 else print('No wins by keeping')
