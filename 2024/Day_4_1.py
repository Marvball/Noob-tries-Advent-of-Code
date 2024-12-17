#DAY_4_1

matrix = []
answer = 0

''' load Matrix from file '''
with open("input.txt", "r") as file:
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
  for row in range(len(matrix)):
    for column in range(len(matrix[row])):
      if matrix[row][column] == "X":
        try:
          if matrix[row][column+1] == "M":
            if matrix[row][column+2] == "A":
              if matrix[row][column+3] == "S":
#                print(f"h_l_r: {row=} {column=}")
                answer += 1
        except:
          continue

def horizontal_right_left():
  global answer
  for row in range(len(matrix)):
    for column in range(len(matrix[row])):
      if matrix[row][column] == "X":
        try:
          if matrix[row][column-1] == "M" and column-1 >= 0:
            if matrix[row][column-2] == "A" and column-2 >= 0:
              if matrix[row][column-3] == "S" and column-3 >= 0:
#                print(f"h_r_l: {row=} {column=}")
                answer += 1
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
#                print(f"v_t_b: {row=} {column=}")
                answer += 1
        except:
          continue

def vertical_bottom_top():
  global answer
  for row in range(len(matrix)):
    for column in range(len(matrix[row])):
      if matrix[row][column] == "X":
        try:
          if matrix[row-1][column] == "M" and row-1 >= 0:
            if matrix[row-2][column] == "A" and row-2 >= 0:
              if matrix[row-3][column] == "S" and row-3 >= 0:
#                print(f"v_b_t: {row=} {column=}")
                answer += 1
        except:
          continue

def diagonal_tl_br():
  global answer
  for row in range(len(matrix)):
    for column in range(len(matrix[row])):
      if matrix[row][column] == "X":
        try:
          if matrix[row+1][column+1] == "M":
            if matrix[row+2][column+2] == "A":
              if matrix[row+3][column+3] == "S":
#                print(f"d_tl_br: {row=} {column=}")
                answer += 1
        except:
          continue 

def diagonal_bl_tr():
  global answer
  for row in range(len(matrix)):
    for column in range(len(matrix[row])):
      if matrix[row][column] == "X":
        try:
          if matrix[row-1][column+1] == "M" and row-1 >= 0:
            if matrix[row-2][column+2] == "A" and row-2 >= 0:
              if matrix[row-3][column+3] == "S" and row-3 >= 0:
#                print(f"d_bl_tr: {row=} {column=}")
                answer += 1
        except:
          continue

def diagonal_br_tl():
  global answer
  for row in range(len(matrix)):
    for column in range(len(matrix[row])):
      if matrix[row][column] == "X":
        try:
          if matrix[row-1][column-1] == "M" and column-1 >= 0 and row-1 >= 0:
            if matrix[row-2][column-2] == "A" and column-2 >= 0 and row-2 >= 0:
              if matrix[row-3][column-3] == "S" and column-3 >= 0 and row-3 >= 0:
#                print(f"d_br_tl: {row=} {column=}")
                answer += 1
        except:
          continue

def diagonal_tr_bl():
  global answer
  for row in range(len(matrix)):
    for column in range(len(matrix[row])):
      if matrix[row][column] == "X":
        try:
          if matrix[row+1][column-1] == "M" and column-1 >= 0:
            if matrix[row+2][column-2] == "A" and column-2 >= 0:
              if matrix[row+3][column-3] == "S" and column-3 >= 0:
#                print(f"d_tr_bl: {row=} {column=}")
                answer += 1
        except:
          continue


horizontal_left_right()
horizontal_right_left()
vertical_top_bottom()
vertical_bottom_top()
diagonal_tl_br()
diagonal_bl_tr()
diagonal_br_tl()
diagonal_tr_bl()
print(f"Final answer: {answer}")
