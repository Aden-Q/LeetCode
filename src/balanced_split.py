import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def balancedSplitExists(arr):
  # Write your code here
  size = len(arr)
  if size == 0:
    return True
  elif size <= 2:
    return False
  
  arr_sort = sorted(arr)
  lptr = 0
  rptr = size - 1
  sum_A = arr_sort[lptr]
  sum_B = arr_sort[rptr]
  while lptr < rptr:
    # condition check
    if lptr + 1 == rptr and sum_A == sum_B and arr_sort[lptr] < arr_sort[rptr]:
      return True

    if sum_A < sum_B:
      # move left pointer
      lptr += 1
      sum_A += arr_sort[lptr]
    else:
      # move right pointer
      rptr -= 1
      sum_B += arr_sort[rptr]
      
  return False
    
    









# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printString(string):
  print('[\"', string, '\"]', sep='', end='')

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
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  arr_1 = [2, 1, 2, 5]
  expected_1 = True
  output_1 = balancedSplitExists(arr_1)
  check(expected_1, output_1)

  arr_2 = [3, 6, 3, 4, 4]
  expected_2 = False
  output_2 = balancedSplitExists(arr_2)
  check(expected_2, output_2)

  # Add your own test cases here
  