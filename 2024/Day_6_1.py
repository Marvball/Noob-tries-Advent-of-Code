# Day 6_1
from IPython.display import clear_output
from time import sleep

answer = 0

rows = 0
columns = 0
guard_position = [0, 0]
guard_facing = ""
walk_path = []
on_matrix = True

with open("input_day6.txt", "r") as file:
  text = file.read().splitlines()
matrix = [list(line) for line in text]

rows = len(matrix)
columns = len(matrix[0])

#initial search for the guard
def find_guard():
  global guard_position
  global guard_facing
  global matrix
  for line in matrix:
    for letter in line:
      if letter == "^":
        guard_position = [matrix.index(line), line.index(letter)]
        guard_facing = "up"
      elif letter == "v":
        guard_position = [matrix.index(line), line.index(letter)]
        guard_facing = "down"
      elif letter == ">":
        guard_position = [matrix.index(line), line.index(letter)]
        guard_facing = "right"
      elif letter == "<":
        guard_position = [matrix.index(line), line.index(letter)]
        guard_facing = "left"

def make_move(direction):
  global guard_facing
  global guard_position
  global matrix
  global walk_path
  safe_walk_path()
  if guard_facing == "up":
    matrix[guard_position[0]][guard_position[1]] = "X"
    guard_position = [guard_position[0]-1, guard_position[1]]
    matrix[guard_position[0]][guard_position[1]] = "^"
  if guard_facing == "right":
    matrix[guard_position[0]][guard_position[1]] = "X"
    guard_position = [guard_position[0], guard_position[1]+1]
    matrix[guard_position[0]][guard_position[1]] = ">"
  if guard_facing == "down":
    matrix[guard_position[0]][guard_position[1]] = "X"
    guard_position = [guard_position[0]+1, guard_position[1]]
    matrix[guard_position[0]][guard_position[1]] = "v"
  if guard_facing == "left":
    matrix[guard_position[0]][guard_position[1]] = "X"
    guard_position = [guard_position[0], guard_position[1]-1]
    matrix[guard_position[0]][guard_position[1]] = "<"

def make_right_turn():
  global guard_facing
  if guard_facing == "up":
    guard_facing = "right"
  elif guard_facing == "right":
    guard_facing = "down"
  elif guard_facing == "down":
    guard_facing = "left"
  elif guard_facing == "left":
    guard_facing = "up"

def check_collision():
  global guard_facing
  global guard_position
  global matrix
  global on_matrix
  if guard_facing == "up":
    if guard_position[0]-1 >= 0:
      if matrix[guard_position[0]-1][guard_position[1]] != "#":
        make_move("up")
      else:
        make_right_turn()
    else:
      on_matrix = False
  elif guard_facing == "down":
    if guard_position[0]+1 <= rows-1:
      if matrix[guard_position[0]+1][guard_position[1]] != "#":
        make_move("down")
      else:
        make_right_turn()
    else:
      on_matrix = False
  elif guard_facing == "right":
    if guard_position[1]+1 <= columns-1: 
      if matrix[guard_position[0]][guard_position[1]+1] != "#":
        make_move("right")
      else:
        make_right_turn()
    else:
      on_matrix = False
  elif guard_facing == "left":
    if guard_position[1]-1 >= 0:
      if matrix[guard_position[0]][guard_position[1]-1] != "#":
        make_move("left")
      else:
        make_right_turn()
    else:
      on_matrix = False

def safe_walk_path():
  global walk_path
  global guard_position
  walk_path.append(guard_position)
#  print(walk_path)

def print_matrix():
  global guard_position
  global guard_facing
  global matrix
#  sleep(0.2)
  
#  print(f"{guard_position= }")
#  print(f"{guard_facing= }")
#  print()
  for line in matrix:
    print(" ".join(line))



###### Programm start######
find_guard()

while on_matrix:   #while guard is on the map (while on_matrix = True)
  check_collision()
#  print_matrix()
#  print(on_matrix)
#  sleep(1)
#  clear_output()

# safe guards last position in list
matrix[guard_position[0]][guard_position[1]] = "X"
safe_walk_path()

walk_path_set = set(tuple(item) for item in walk_path) #convert walk_path list in set of tuples to clear it from duplicates
answer = len(walk_path_set)
print(f"Final answer: {answer}\n")

for line in matrix:
  print(" ".join(line)) #print final Matrix
