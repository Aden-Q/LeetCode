import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def getTotalTime(arr):
  # Write your code here
  arr_copy = arr.copy()
  arr_copy.sort()
  penalty_sum = 0
  
  for i in range(1, len(arr)+1):
    penalty_sum += i * arr_copy[i-1]
  penalty_sum -= arr_copy[-1]

  return penalty_sum
  









# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  arr_1 = [4, 2, 1, 3]
  expected_1 = 26
  output_1 = getTotalTime(arr_1)
  check(expected_1, output_1)

  arr_2 = [2, 3, 9, 8, 4]
  expected_2 = 88
  output_2 = getTotalTime(arr_2)
  check(expected_2, output_2)

  # Add your own test cases here
  arr_3 = [2]
  expected_3 = 0
  output_3 = getTotalTime(arr_3)
  check(expected_3, output_3)
  