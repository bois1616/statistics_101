import random
from icecream import ic  # type: ignore

# Konfiguriere das Ausgabeformat
def custom_output(output):
    prefix = "DEBUG | "
    # Extrahiere den tatsächlichen String aus dem output
    actual_output = output.split("': ")[-1].strip().strip("'")
    actual_output = bytes(actual_output, "utf-8").decode("unicode_escape")
    # print(f'{output=}\t{actual_output=}')
    print(prefix + actual_output)


ic.configureOutput(includeContext=False, outputFunction=custom_output)
# ic.disable()


def mh_sim_sr(choice: int, doors: list) -> int:
    """
    Monty Hall Simulation
    Params:
    choice: int - the door the player chooses
    doors: list - the doors available (col1) and the car location (col2)
    Returns:
    int - the last choice of the player
    """
    nr_doors = len(doors)
    assert choice < nr_doors, "Invalid choice"
    assert sum(doors) == 1, "There must be exactly one car"

    # Monty opens a random door (not the player's choice and not the car)
    other = random.choice(
        [door for door in range(nr_doors) if door != choice and not doors[door]]
    )
    ic(f"Monty opens door {other + 1}")

    # Player switches to the other door?
    if random.random() > 0.5:
        # Player changes the door"
        new_choice = random.choice(
            [door for door in range(nr_doors) if door != choice and door != other]
        )
    else:
        # Player keeps the door
        new_choice = choice

    ic(f"choice (origin): {choice + 1}\tchoice (new): {new_choice + 1}")

    # Player wins if the car is behind the chosen door
    return new_choice


def shuffle_doors(n_doors: int = 3) -> list:
    doors = [False for _ in range(n_doors)]
    doors[random.randint(0, n_doors - 1)] = True

    return doors


if __name__ == "__main__":
    n_doors = 3
    n_runs = 30000
    ic.disable() if n_runs > 50 else None

    # result, change = mh_sim_sr(choice, doors)
    win_keep = win_change = 0
    for _ in range(n_runs):
        ic("\n")
        ic(f"Run: {_ + 1}")
        # setup new game
        doors = shuffle_doors(n_doors)
        ic(f"{doors=}")
        # player chooses a door
        choice = random.randint(0, n_doors - 1)

        ic(f"Car behind door {doors.index(True) + 1}\tChoice: {choice + 1}")

        new_choice = mh_sim_sr(choice, doors)
        win = doors[new_choice]
        switch = new_choice != choice

        ic(
            f"Player {'wins' if win else 'looses'}\twith {'switching' if switch else 'keeping'} (new choice: {new_choice + 1})"
        )

        if win:
            if switch:
                win_change += 1
            else:
                win_keep += 1

    print(
        f"{n_runs} runs\nWins by changing:\t{win_change}\tWins by keeping: {win_keep}"
    )
    if win_keep > 0:
        print(f"Ratio W_c/W_k: {win_change / win_keep:.2f}")
    else:
        print("No wins by keeping")
