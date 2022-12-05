def main():
  rucksacks = []

  with open('input.txt') as file:
    for line in file:
      rucksacks.append(line.rstrip('\n'))
  file.close()

  dupes = []
  priorities = 0
  
  for rucksack in rucksacks:
    a = rucksack[:int(len(rucksack)/2)]
    b = rucksack[int(len(rucksack)/2):]
    for char in a:
      if char in b:
        dupes.append(char)
        break
  
  for char in dupes:
    if char.islower():
      priority = ord(char) - 96
    elif char.isupper():
      priority = ord(char) - 38
    priorities += priority

  print(dupes)
  print(len(dupes))
  print(priorities)

main()
