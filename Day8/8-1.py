def main():
  trees = []
  visible_trees = []

  with open('input.txt') as file:
    for line in file:
      line = line.rstrip('\n')   # get rid of \n
      line = [int(x) for x in line]   # list comprehension to split each row of trees into individual trees; then cast to make each digit an int
      zeros_line = [0 for x in line]   # zeros, for the visibility array
      trees.append(line)   # end result is a nested list of ints
      visible_trees.append(zeros_line)   # same for the visibility array
  file.close()

  tallest_in_row = 0
  tallest_in_col = 0
  count = 0

  # First we nested loop once - from top->bottom, and left->right
  for row in range(len(trees[0])):
    tallest_in_row = 0

    for column in range(len(trees[0])):
      if row == 0:
        visible_trees[row][column] = 1
        count += 1
        tallest_in_col = trees[column][row]
      elif row == len(trees)-1:
        visible_trees[row][column] = 1
        count += 1
      elif column == 0:
        visible_trees[row][column] = 1
        count += 1
        tallest_in_row = trees[row][column]
      elif column == len(trees[row])-1:
        visible_trees[row][column] = 1
        count += 1
      
      # otherwise, we're in the interior. evaluation logic for the interior:
      else:
        # see if the current tree is taller than the ones before it IN THAT COLUMN
        if trees[column][row] > tallest_in_col:
          visible_trees[column][row] = 1
          count += 1
          tallest_in_col = trees[column][row]

        # see if the current tree is taller than the ones before it IN THAT ROW
        if trees[row][column] > tallest_in_row:
          visible_trees[row][column] = 1
          count += 1
          tallest_in_row = trees[row][column]

  # reverse the outer trees list
  reversed_trees = trees[::-1]

  # Then we nested loop once more - from "bottom"->"top", and "right"->"left"
  for row in range(len(trees[0])):

    for column in range(len(trees[0])):
      if row == 0:
        tallest_in_col = reversed_trees[column][row]

      elif row == len(reversed_trees)-1:
        # do nothing, we've already handled this case
        pass

      elif column == 0:
        tallest_in_row = reversed_trees[row][column]

      elif column == len(reversed_trees[row])-1:
        # do nothing, we've already handled this case
        pass
    
      else:
        if reversed_trees[column][row] > tallest_in_col:
          visible_trees[column][row] = 1
          count += 1
          tallest_in_col = reversed_trees[column][row]

        if reversed_trees[row][column] > tallest_in_row:
          visible_trees[row][column] = 1
          count += 1
          tallest_in_row = reversed_trees[row][column]

  print(count)
  count = 0
  for row in range(len(trees[0])):
    for column in range(len(trees[0])):
      if visible_trees[row][column] == 1:
        count += 1
  print(count)

main()