import math
# Add any extra import statements you may need here
import heapq


# Add any helper functions you may need here

def negate_arr(arr, size):
  for i in range(size):
    arr[i] = -arr[i]
    

def maxCandies(arr, k):
  # Write your code here
  res = 0  # sum up the candy to eat
  arr_copy = arr.copy()
  negate_arr(arr_copy, len(arr_copy))
  heapq.heapify(arr_copy)
  
  for i in range(k):
    num_candy = heapq.heappop(arr_copy)
    res += -num_candy
    heapq.heappush(arr_copy, -(-num_candy // 2))
    
  return res




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
  n_1, k_1 = 5, 3
  arr_1 = [2, 1, 7, 4, 2]
  expected_1 = 14
  output_1 = maxCandies(arr_1, k_1)
  check(expected_1, output_1)

  n_2, k_2 = 9, 3
  arr_2 = [19, 78, 76, 72, 48, 8, 24, 74, 29]
  expected_2 = 228
  output_2 = maxCandies(arr_2, k_2)
  check(expected_2, output_2)

  # Add your own test cases here
  