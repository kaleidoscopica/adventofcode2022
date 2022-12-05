def main():
  rucksacks = []

  with open('input.txt') as file:
    for line in file:
      rucksacks.append(line.rstrip('\n'))
  file.close()

  set_of_3 = []
  badges = []
  priorities = 0

  for rucksack in rucksacks:
    set_of_3.append(rucksack)
    if len(set_of_3) == 3:
      for char in set_of_3[0]:
        if char in set_of_3[1]:
          if char in set_of_3[2]:
            badges.append(char)
      set_of_3 = []
  
  for char in badges:
    if char.islower():
      priority = ord(char) - 96
    elif char.isupper():
      priority = ord(char) - 38
    priorities += priority

  print(badges)
  print(priorities)

main()
