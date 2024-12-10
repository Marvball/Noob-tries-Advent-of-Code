#DAY_4_1
matrix = []

with open("test_input.txt", "r") as file:
  txt = file.read().split("\n")
  for lines in txt:
    matrix.append(lines.split())

print(matrix)


###### Work in Progress #########
