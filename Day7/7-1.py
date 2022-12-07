def main():
  stack = []
  files = []
  import itertools

  with open('input.txt') as file:
    data = file.read()
  file.close()

  for line in data.splitlines():
    # if we're changing directories further up the tree, 
    if line == '$ cd ..':
      # pop the last element on stack and return it as 'size',
      size = stack.pop()
      # append that size to the files list,
      files.append(size)
      # and add the size to that of the last element on the stack
      stack[-1] += size
    # if we're changing directories down into the tree, append an empty placeholder at the end of the stack; we'll add to this later
    elif line.startswith('$ cd '):
      stack.append(0)
    # if the first char in the line is a digit, it's a file size - add its size to that of the last element on the stack
    elif line[0].isdigit():
      stack[-1] += int(line.split()[0])

  # starting at the last element and going backward, accumulate the sizes and then extend the files list with them
  files.extend(itertools.accumulate(stack[::-1]))

  print(sum(size for size in files if size <= 100_000))

main()