#DAY_3_1

answer = 0

with open("input.txt", "r") as file:
  data = file.read()
  list = re.findall("mul\((\d+),(\d+)\)", data)
  print(list)
  for item in list:
    x = int(item[0])
    y = int(item[1])
    answer += x * y

print(answer)
