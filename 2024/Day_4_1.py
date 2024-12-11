#DAY_4_1

import re

matrix = []
answer = 0

''' load Matrix from file '''
with open("test_input.txt", "r") as file:
  text = file.read().split("\n")
#  print(text)
for line in text:
  line_list = [letter for letter in line]
#  print(line_list)
  matrix.append(line_list)
#print(matrix)


''' scan for XMAS in horizontal lines '''
def horizontal_left_right():
  global answer
  for row in matrix:
    try:
      for i in range(len(row)):
        if row[i] == "X":
          if row[i+1] == "M":
            if row[i+2] == "A":
              if row[i+3] == "S":
                answer += 1
                print(f"Answer{answer}: horizontal {row[i]}{row[i+1]}{row[i+2]}{row[i+3]}")
    except:
      continue

def horizontal_right_left():
  global answer
  for row in matrix:
    try:
      for i in range(len(row)):
        if row[i] == "S":
          if row[i+1] == "A":
            if row[i+2] == "M":
              if row[i+3] == "X":
                answer += 1
                print(f"Answer{answer}: horizontal {row[i]}{row[i+1]}{row[i+2]}{row[i+3]}")
    except:
      continue

''' scan for XMAS in vertical lines '''
def vertical_top_bottom():
  global answer
  for row in range(len(matrix)):
    for column in range(len(matrix[row])):
      if matrix[row][column] == "X":
        try:
          if matrix[row+1][column] == "M":
            if matrix[row+2][column] == "A":
              if matrix[row+3][column] == "S":
                print(f"{row=}{column=}")
                answer += 1
        except:
          continue

def vertical_bottom_top():
  global answer
  for row in range(len(matrix)):
    for column in range(len(matrix[row])):
      if matrix[row][column] == "X":
        try:
          if matrix[row-1][column] == "M":
            if matrix[row-2][column] == "A":
              if matrix[row-3][column] == "S":
                print(f"{row=}{column=}")
                answer += 1
        except:
          continue
        
   




#horizontal_left_right()
#horizontal_right_left()
#vertical_top_bottom()
vertical_bottom_top()
print(f"Final answer: {answer}")


###### Work in Progress #########
