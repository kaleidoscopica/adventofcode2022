def main():
  with open('input.txt') as file:
    message = file.readline()
  file.close()

  index = 1
  sop_marker = []

  for char in message:
    # add the character to the list
    sop_marker.append(char)
    # if the length of the list is greater than a set made from the list, there's a duplicate in it! remove the earliest entry to 'shift the window'
    while len(sop_marker) > len(set(sop_marker)):
      del sop_marker[0]
    # if the list has reached length 14, that's our marker - break
    if len(sop_marker) == 14:
      print(sop_marker)
      break
    index += 1

  print("The index of the start-of-message marker is:", index)

main()