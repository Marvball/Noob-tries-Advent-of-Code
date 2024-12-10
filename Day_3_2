#DAY_3_2
import re
answer = 0
do_switch = 1
answer_list = []

with open("input.txt", "r") as file:
  data = file.read()
  list = re.split("(don't\(\))|(do\(\))|(mul\((\d+),(\d+)\))", data)
#print(list)

for item in list:
  if item == "do()":
    do_switch = 1
  if item == "don't()":
    do_switch = 0
  
  if item is not None and do_switch==1:
    if "mul(" in item:
      #print(item)
      answer_list.append(re.findall("mul\((\d+),(\d+)\)", item))

#print(answer_list)

for item in answer_list:
  for s in item:
    x = int(s[0])
    y = int(s[1])
    answer += x * y

print(answer)
