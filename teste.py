from one_battle import running

move1 : int = 0
move2 : int = 0
move3 : int = 0
move4 : int = 0
level : int = 0
_viable = 0.0
abort = 0.0

running(move1, move2, move3, move4, level, _viable, abort)

print("viable: " + str(_viable))
print("abort: " + str(abort))