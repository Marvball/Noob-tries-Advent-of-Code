#DAY_4_2
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

def tlbr_trbl():
  global answer
  for row in range(len(matrix)):
    for column in range(len(matrix[row])):
      if matrix[row][column] == "A":
        if column-1 >= 0 and row-1 >= 0:
          try:          
            if matrix[row-1][column-1] == "M":
              if matrix[row+1][column+1] == "S":
                if matrix[row-1][column+1] == "M":
                  if matrix[row+1][column-1] == "S":
#                    print(f"tlbr_trbl: {row=} {column=}")
                    answer += 1
          except:
            continue

def tlbr_bltr():
  global answer
  for row in range(len(matrix)):
    for column in range(len(matrix[row])):
      if matrix[row][column] == "A":
        if column-1 >= 0 and row-1 >= 0:
          try:          
            if matrix[row-1][column-1] == "M":
              if matrix[row+1][column+1] == "S":
                if matrix[row+1][column-1] == "M":
                  if matrix[row-1][column+1] == "S":
#                    print(f"tlbr_bltr: {row=} {column=}")
                    answer += 1
          except:
            continue

def brtl_bltr():
  global answer
  for row in range(len(matrix)):
    for column in range(len(matrix[row])):
      if matrix[row][column] == "A":
        if column-1 >= 0 and row-1 >= 0:
          try:          
            if matrix[row+1][column+1] == "M":
              if matrix[row-1][column-1] == "S":
                if matrix[row+1][column-1] == "M":
                  if matrix[row-1][column+1] == "S":
#                    print(f"brtl_bltr: {row=} {column=}")
                    answer += 1
          except:
            continue

def brtl_trbl():
  global answer
  for row in range(len(matrix)):
    for column in range(len(matrix[row])):
      if matrix[row][column] == "A":
        if column-1 >= 0 and row-1 >= 0:
          try:          
            if matrix[row+1][column+1] == "M":
              if matrix[row-1][column-1] == "S":
                if matrix[row-1][column+1] == "M":
                  if matrix[row+1][column-1] == "S":
#                    print(f"brtl_trbl: {row=} {column=}")
                    answer += 1
          except:
            continue

tlbr_trbl()
tlbr_bltr()
brtl_bltr()
brtl_trbl()


print(f"Final answer: {answer}")
