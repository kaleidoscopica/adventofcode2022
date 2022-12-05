def main():
  data = []
  point_dict = {
    'B X': 1,
    'C Y': 2,
    'A Z': 3,
    'A X': 4,
    'B Y': 5,
    'C Z': 6,
    'C X': 7,
    'A Y': 8,
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
