import sys
import os

sys.path.append('D:\Downloads\Estudo\Coisas do Lab\Optimization\pokemon-python-master')

import sim.sim as sim
from tools.pick_six import generate_team, generate_giovanni_team, generate_pokemon
from sim.player import pokemon_left
import time

#move1 = 33
#move2 = 100
#move3 = 70
#move4 = 6
#level = 100
abort = 0
hp = -10000
faint = 0

if move1 != move2 and move1 != move3 and move1 != move4 and move2 != move3 and move2 != move4 and move3 != move4:
  
  teams = []
  teams.append(sim.dict_to_team_set(generate_pokemon(move1, move2, move3, move4, level)))
  teams.append(sim.dict_to_team_set(generate_giovanni_team()))
  for i in range(500):
    battle = sim.Battle('single', 'Guilherme', teams[0], 'Giovanni', teams[1], debug=True)
    log_dir = f"logs/{teams[0][0].species}"
    if not os.path.exists(log_dir):
      os.makedirs(log_dir)
    with open(f"logs/{teams[0][0].species}/level_{level}_move1_{move1}_move2_{move2}_move3_{move3}_move4_{move4}.txt", "w") as f:
      sys.stdout = f
      sim.run(battle)
    sys.stdout = sys.__stdout__
    hp = battle.p1.active_pokemon[0].hp
    faint = int(battle.p1.active_pokemon[0].fainted)
    if battle.p1.active_pokemon[0].hp > 0 and battle.p1.active_pokemon[0].fainted == False or battle.p1.active_pokemon[0].hp < -10000:
      break
  if hp < 0 or faint == True:
    os.remove(f"logs/{teams[0][0].species}/level_{level}_move1_{move1}_move2_{move2}_move3_{move3}_move4_{move4}.txt")
    
else:
  abort = 1