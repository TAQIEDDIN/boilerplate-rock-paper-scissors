from RPS_game import play
from RPS_bots import player, quincy  # Assuming quincy is another bot

# Play 1000 games between your player and Quincy
play(player, quincy, 1000, verbose=True)
