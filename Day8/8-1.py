def main():
  trees = []
  visible_trees = []

  with open('input.txt') as file:
    for line in file:
      line = line.strip()   # get rid of \n
      line = [int(x) for x in line]   # list comprehension to split each row of trees into individual trees; then cast to make each digit an int
      trees.append(line)   # end result is a nested list of ints
      zeros_line = [0 for x in line]   # zeros, for the visibility array
      visible_trees.append(zeros_line)   # same for the visibility array
  file.close()

  tallest_in_row = 0
  tallest_in_col = 0

  # First we nested loop once - this one sets the outside perimeter, and checks rows left->right
  for row in range(len(trees[0])):
    tallest_in_row = trees[row][0]
    for column in range(len(trees[0])):
      if row == 0:
        visible_trees[row][column] = 1
      elif row == len(trees[0])-1:
        visible_trees[row][column] = 1
      elif column == 0:
        visible_trees[row][column] = 1
      elif column == len(trees[0])-1:
        visible_trees[row][column] = 1
      
      # otherwise, we're in the interior. evaluation logic for the interior:
      elif trees[row][column] > tallest_in_row:
          visible_trees[row][column] = 1
          tallest_in_row = trees[row][column]
    ### column logic complete for a single row

    # now reverse the rows and do the same check, to check from "right"->"left" 
    trees[row].reverse()   # REVERSE THE ROW
    tallest_in_row = trees[row][0]
    for column in range(len(trees[0])):
      if column == 0 or row == 0 or column == len(trees[0])-1 or row == len(trees[0])-1:
        pass
      # otherwise, we're in the interior. evaluation logic for the interior:
      elif trees[row][column] > tallest_in_row:
        visible_trees[row].reverse()   # flip the mapped row once to mark the correct tree
        visible_trees[row][column] = 1
        visible_trees[row].reverse()   # then flip it back - not very efficient :) 
        tallest_in_row = trees[row][column]
    # put the row back how it should be
    trees[row].reverse()

  # Another loop, to check the columns top->bottom:
  for column in range(len(trees[0])):
    tallest_in_col = trees[0][column]
    for row in range(len(trees[0])):
      if column == 0 or row == 0 or column == len(trees[0])-1 or row == len(trees[0])-1:
        pass
      elif trees[row][column] > tallest_in_col:
        visible_trees[row][column] = 1
        tallest_in_col = trees[row][column]

  # now need to flip things upside down
  trees = trees[::-1]
  visible_trees = visible_trees[::-1]

  ## and repeat the column check to check "bottom"->"top":
  for column in range(len(trees[0])):
    tallest_in_col = trees[0][column]
    for row in range(len(trees[0])):
      if column == 0 or row == 0 or column == len(trees[0])-1 or row == len(trees[0])-1:
        pass
      elif trees[row][column] > tallest_in_col:
        visible_trees[row][column] = 1
        tallest_in_col = trees[row][column]

  # flip them back I guess
  trees = trees[::-1]
  visible_trees = visible_trees[::-1]

  # Now we should have a count we can tally up from within the visible_trees map
  count = 0
  for row in range(len(trees[0])):
    for column in range(len(trees[0])):
      if visible_trees[row][column] == 1:
        count += 1
  print(count)

main()