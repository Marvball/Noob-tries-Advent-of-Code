# Day_5_2
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


all_updated = False
while all_updated == False:
  all_updated = True
  for list in update_lists:
    for rule in ordering_rules:
      if rule[0] in list and rule[1] in list:
        if list.index(rule[0]) > list.index(rule[1]):
          list.append("rb")
          all_updated = False
          list.remove(rule[0])
          list.insert(0, rule[0])
print("Fertig")

for list in update_lists:
  if "rb" in list:
    while "rb" in list:
      list.remove("rb")
      print(list)
    answer += list[len(list)//2]

print(answer)
