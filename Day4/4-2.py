def main():
  assignments = []
  with open('input.txt') as file:
    for line in file:
      assignments.append(line.rstrip('\n'))
  file.close()

  overlaps = 0

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

    overlaps_a = False
    overlaps_b = False

    for number in range_a:
      if number in range_b:
        overlaps_a = True
        break
    
    for number in range_b:
      if number in range_a:
        overlaps_b = True
        break
    
    if overlaps_a == True or overlaps_b == True:
      overlaps += 1

  print("Number of overlaps is:", overlaps)

main()