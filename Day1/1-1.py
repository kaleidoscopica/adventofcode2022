def main():
  calorie_data = []

  with open('input.txt') as file:
    for line in file:
      if line == "\n":
        line = line.replace("\n", "space")
        calorie_data.append(line)
      else:
        calorie_data.append(int(line.strip()))
    calorie_data.append("space")
  file.close()

  sum_per_elf = 0
  maximum_sum = 0

  for item in calorie_data:
    if item != "space":
      sum_per_elf += item
    elif item == "space":
      if sum_per_elf > maximum_sum:
        maximum_sum = sum_per_elf
      sum_per_elf = 0

  print(calorie_data)
  print("Most calories from one elf: ", maximum_sum)

main()
