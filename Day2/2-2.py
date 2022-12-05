def main():
  data = []
  point_dict = {
    'B X': 1,
    'C X': 2,
    'A X': 3,
    'A Y': 4,
    'B Y': 5,
    'C Y': 6,
    'C Z': 7,
    'A Z': 8,
    'B Z': 9
  }
  
  with open('input.txt') as file:
    for line in file:
      data.append(line.rstrip('\n'))
  file.close()

  point_total = 0
  for item in data:
    point_total += point_dict[item]

  print(point_total)

main()
