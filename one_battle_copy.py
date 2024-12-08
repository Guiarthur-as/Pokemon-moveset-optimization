import sys

sys.path.append('C:/Users/Guilherme/Downloads/Guilherme_Faculdade/Optimization/pokemon-python-master')

import sim.sim as sim
from tools.pick_six import generate_team, generate_giovanni_team, generate_pokemon
import os

move1 : int = 76
move2 : int = 82
move3 : int = 8
move4 : int = 50
level : int = 29
abort = 0
hp = -10000

if move1 != move2 and move1 != move3 and move1 != move4 and move2 != move3 and move2 != move4 and move3 != move4:
  
  for i in range(500):
    teams = []
    teams.append(sim.dict_to_team_set(generate_pokemon(move1, move2, move3, move4, level)))
    teams.append(sim.dict_to_team_set(generate_giovanni_team()))
    battle = sim.Battle('single', 'Guilherme', teams[0], 'Giovanni', teams[1], debug=True)
    log_dir = f"logs/{teams[0][0].species}"
    if not os.path.exists(log_dir):
      os.makedirs(log_dir)
    with open(f"logs/{teams[0][0].species}/level_{level}_move1_{move1}_move2_{move2}_move3_{move3}_move4_{move4}.txt", "w") as f:
      sys.stdout = f
      sim.run(battle)
    sys.stdout = sys.__stdout__
    if battle.p1.active_pokemon[0].hp > 0:
      break
  hp = battle.p1.active_pokemon[0].hp
  print(hp)

    
else:
  abort = 1

