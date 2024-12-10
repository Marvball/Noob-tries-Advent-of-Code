#DAY 1

list_a = []
list_b = []
over_all_distance = 0
similarity_score = 0

with open("day1_data.txt", "r", encoding="utf-8") as f:
  global list_a
  global list_b
  lines = f.read().split("\n")
  for line in lines:
    list_a.append(int(line[0:5]))
    list_b.append(int(line[-6:]))

list_a.sort()
list_b.sort()

for i in range(len(list_a)):
  global over_all_distance
  global similarity_score
  a = list_a[i]
  b = list_b[i]
  c = b - a
  result = abs(c)
  over_all_distance += result

  d = list_a[i]
  e = list_b.count(d)
  f = d * e
  similarity_score += f



print(f"{over_all_distance=}")
print(f"{similarity_score=}")


