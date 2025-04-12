import random

# This function will play against various bots in the challenge
def player(prev_play: str, opponent_history = []):
    # If it's the first move, choose randomly
    if prev_play == "":
        return random.choice(["R", "P", "S"])
    
    # Store opponent's previous move
    opponent_history.append(prev_play)
    
    # Simple strategy: Counter the opponent's last move
    last_opponent_move = opponent_history[-1]
    
    if last_opponent_move == "R":
        return "P"  # Paper beats Rock
    elif last_opponent_move == "P":
        return "S"  # Scissors beats Paper
    elif last_opponent_move == "S":
        return "R"  # Rock beats Scissors

    # If no matching strategy is found, choose randomly
    return random.choice(["R", "P", "S"])
