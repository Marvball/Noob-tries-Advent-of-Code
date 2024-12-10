#DAY 2 - 2
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

def check(list):
  if (check_const_decrease(list) or check_const_increase(list)) and check_little_steps(list):
    return True
  else:
    return False


with open("day2_data.txt", "r", encoding="utf-8") as f:
  lines = f.read().split("\n")
  for line in lines:
    numbers = line.split(" ")
    int_numbers = list(map(int, numbers))

    if check(int_numbers):
#      print(f"{check(int_numbers)}")
      count_is_safe += 1
      continue
    else:
      for i in range(len(int_numbers)):
        new_list = list(int_numbers)
        new_list.pop(i)
        if check(new_list):
#          print(f"{check(new_list)=}")
          count_is_safe += 1
          break

print(f"{count_is_safe=}")
