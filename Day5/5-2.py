def main():
  crate_data = []
  with open('input.txt') as file:
    for line in file:
      crate_data.append(line.rstrip('\n'))
  file.close()

  # converts the crate data into listing them by column
  # I know there's a shorter way to do this but this way helped me think through it better ¯\_(ツ)_/¯
  crate_locs = [1, 5, 9, 13, 17, 21, 25, 29, 33]
  col1_crates = []
  col2_crates = []
  col3_crates = []
  col4_crates = []
  col5_crates = []
  col6_crates = []
  col7_crates = []
  col8_crates = []
  col9_crates = []

  for index, position in enumerate(crate_locs):
    for idx, item in enumerate(crate_data):
      if idx < 8 and crate_data[idx][position] != ' ':
        if index == 0:
          col1_crates.append(crate_data[idx][position])
        elif index == 1:
          col2_crates.append(crate_data[idx][position])
        elif index == 2:
          col3_crates.append(crate_data[idx][position])
        elif index == 3:
          col4_crates.append(crate_data[idx][position])
        elif index == 4:
          col5_crates.append(crate_data[idx][position])
        elif index == 5:
          col6_crates.append(crate_data[idx][position])
        elif index == 6:
          col7_crates.append(crate_data[idx][position])
        elif index == 7:
          col8_crates.append(crate_data[idx][position])
        elif index == 8:
          col9_crates.append(crate_data[idx][position])
  
  crates = [col1_crates, col2_crates, col3_crates, col4_crates, col5_crates, col6_crates, col7_crates, col8_crates, col9_crates]

  print("Before starting...")
  print("Column 1 crates are:", col1_crates)
  print("Column 2 crates are:", col2_crates)
  print("Column 3 crates are:", col3_crates)
  print("Column 4 crates are:", col4_crates)
  print("Column 5 crates are:", col5_crates)
  print("Column 6 crates are:", col6_crates)
  print("Column 7 crates are:", col7_crates)
  print("Column 8 crates are:", col8_crates)
  print("Column 9 crates are:", col9_crates)

  # create a list with just the move commands
  # i.e. "move 6 from 4 to 3" becomes [6, 4, 3]
  cmd_list = []
  for idx, item in enumerate(crate_data):
    if idx >= 10:
      cmd_list.append([int(s) for s in item.split() if s.isdigit()])

  for item in cmd_list:
    num_to_move = item[0]
    from_col = item[1]
    to_col = item[2]
    #print("Moving " + str(num_to_move) + " crates from column " + str(from_col) + " to column " + str(to_col) + ".")
    temp_list = []
    for i in range(num_to_move):
      item_removed = crates[from_col-1].pop(0)
      temp_list.append(item_removed)
    # With the CrateMover 9001, the crates are moved all at once
    temp_list.reverse()
    for crate in temp_list:
      crates[to_col-1].insert(0, crate)

  print("After complete...")
  print("Column 1 crates are:", col1_crates)
  print("Column 2 crates are:", col2_crates)
  print("Column 3 crates are:", col3_crates)
  print("Column 4 crates are:", col4_crates)
  print("Column 5 crates are:", col5_crates)
  print("Column 6 crates are:", col6_crates)
  print("Column 7 crates are:", col7_crates)
  print("Column 8 crates are:", col8_crates)
  print("Column 9 crates are:", col9_crates)

  print("The crates on top of each stack, in order, are: " + col1_crates[0] + col2_crates[0] + col3_crates[0] + col4_crates[0] + col5_crates[0] + col6_crates[0] + col7_crates[0] + col8_crates[0] + col9_crates[0])
main()