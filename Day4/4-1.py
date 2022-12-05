def main():
  assignments = []
  with open('input.txt') as file:
    for line in file:
      assignments.append(line.rstrip('\n'))
  file.close()

  fully_contained = 0

  for item in assignments:
    a, b = item.split(',')
    num1, num2 = a.split('-')
    num1 = int(num1)
    num2 = int(num2)
    range_a = list(range(num1, num2+1))
    num3, num4 = b.split('-')
    num3 = int(num3)
    num4 = int(num4)
    range_b = list(range(num3, num4+1))

    fully_contains_a = True
    fully_contains_b = True

    for number in range_a:
      if number not in range_b:
        fully_contains_a = False
        break
    
    for number in range_b:
      if number not in range_a:
        fully_contains_b = False
        break
    
    if fully_contains_a == True or fully_contains_b == True:
      fully_contained += 1

  print(len(assignments))
  print(fully_contained)

main()