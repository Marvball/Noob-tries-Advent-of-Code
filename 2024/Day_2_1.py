#DAY 2 - 1
count_is_safe = 0

def check_const_decrease(list):
  for i in range(len(list)-1):
    if list[i] > list[i+1]:
      continue
    else:
      return False
  return True

def check_const_increase(list):
  for i in range(len(list)-1):
    if list[i] < list[i+1]:
      continue
    else:
      return False
  return True

def check_little_steps(list):
  for i in range(len(list)-1):
    if abs(list[i]-list[i+1]) <= 3:
      continue
    else:
      return False
  return True


with open("day2_data.txt", "r", encoding="utf-8") as f:
  lines = f.read().split("\n")
  for line in lines:
    numbers = line.split(" ")
    int_numbers = list(map(int, numbers))

    if check_little_steps(int_numbers) and (check_const_decrease(int_numbers) or check_const_increase(int_numbers)):

      global count_is_safe
      count_is_safe += 1


print(f"{count_is_safe}")


