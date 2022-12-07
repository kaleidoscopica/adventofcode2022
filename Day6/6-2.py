def main():
  with open('input.txt') as file:
    message = file.readline()
  file.close()

  index = 1
  sop_marker = []

  for char in message:
    # if the char isn't in the set yet, add it
    sop_marker.append(char)
    # if the length of the list is greater than a set made from the list, there's a duplicate in it! remove the earliest entry to 'shift the window'
    while len(sop_marker) > len(set(sop_marker)):
      del sop_marker[0]
    # if the set has reached length 4, that's our marker - break
    if len(sop_marker) == 4:
      print(sop_marker)
      break
    index += 1

  #marker = message[index-4:index]
  print("The index of the start-of-packet marker is:", index)
  #print(marker)

main()