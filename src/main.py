import random

def monty_hall_game(switch_doors):
    doors = ["car", "goat", "goat"]
    random.shuffle(doors)
    
    initial_choice = random.choice(range(len(doors)))
    
    if switch_doors:
        
        revealed_doors = [i for i in range (len(doors)) if i != initial_choice and doors[i] != "car"]
        revealed_door = random.choice(revealed_doors)
        
        final_choice = [i for i in range(len(doors)) if i!= initial_choice and i!= revealed_door] [0]
    else:
        final_choice = initial_choice
    
    return doors[final_choice] == "car"


def monty_hall_simulator(num_of_games):
    num_wins_without_switching = sum ([monty_hall_game(False) for _ in range(num_of_games)])
    num_wins_with_switching = sum ([monty_hall_game(True) for _ in range(num_of_games)])
    
    return ((num_wins_with_switching / num_of_games) * 100) , (num_wins_without_switching / num_of_games) * 100


if __name__ == "__main__":
    num_of_games = 100000
    win_percentage_with_switching, win_percentage_without_switching = monty_hall_simulator(num_of_games)
    print(f"Win percentage with switching: {win_percentage_with_switching} % \nWin percentage without switching: {win_percentage_without_switching} %")