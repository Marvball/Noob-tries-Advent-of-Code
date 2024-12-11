#DAY_4_1
matrix = []
line_number = -1

with open("test_input.txt", "r") as file:
  text = file.read().split("\n")
#  print(text)

for line in text:
  line_list = [letter for letter in line]
#  print(line_list)
  matrix.append(line_list)

print(matrix)


###### Work in Progress #########
