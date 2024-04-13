import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def findSignatureCounts(arr):
  # Write your code here
  # sign at  least once (when each student holds his own yearbook)
  res = [1] * len(arr)
  arr_temp = arr.copy()
  size = len(arr)
  target = []
  # this is the target array we want
  for i in range(size):
    target.append(i+1)
  #  store the resulting array in the next round
  while arr_temp != target:
    temp = arr_temp.copy()
    for i in range(1, size+1):
      # in the case that the yearbook need to be signed and transferred
      if arr_temp[i-1] != i:
        temp[arr_temp[i-1] - 1] = arr_temp[i-1]
        res[i-1] += 1  # sign once
      else:
        continue
    arr_temp = temp
  
  return res
  




# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

def printIntegerList(array):
  size = len(array)
  print('[', end='')
  for i in range(size):
    if i != 0:
      print(', ', end='')
    print(array[i], end='')
  print(']', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  expected_size = len(expected)
  output_size = len(output)
  result = True
  if expected_size != output_size:
    result = False
  for i in range(min(expected_size, output_size)):
    result &= (output[i] == expected[i])
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printIntegerList(expected)
    print(' Your output: ', end='')
    printIntegerList(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  arr_1 = [2, 1]
  expected_1 = [2, 2]
  output_1 = findSignatureCounts(arr_1)
  check(expected_1, output_1)

  arr_2 = [1, 2]
  expected_2 = [1, 1]
  output_2 = findSignatureCounts(arr_2)
  check(expected_2, output_2)


  # Add your own test cases here
  