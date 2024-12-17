# Day_5_1
import re
answer = 0

with open("drive/MyDrive/Colab Notebooks/input_data/input_day5.txt", "r") as file:
  text = file.read().strip()
  sep1, sep2 = text.split("\n\n")
  sep1 = sep1.split("\n")
  sep2 = sep2.split("\n")
  sep2 = [item.split(",") for item in sep2]

print(sep1)
print(sep2)


ordering_rules = []
for item in sep1:
  ordering_rules.append([*map(int, item.split("|"))])

update_lists = []
for item in sep2:
  update_lists.append([*map(int, item)])


for list in update_lists:
  rule_break = False
  for rule in ordering_rules:
    if rule[0] in list and rule[1] in list:
      if list.index(rule[0]) > list.index(rule[1]):
        rule_break = True
  if rule_break == False:
    answer += list[len(list)//2]

print(answer)
