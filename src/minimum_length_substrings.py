import math
# Add any extra import statements you may need here


# Add any helper functions you may need here

def str_contains(s1, s2):
  # check whether all characters in s2 are present in s1
  for c in s2:
    if c not in s1:
      return False

  dict1 = {}
  dict2 = {}
  for c in s2:
    if c not in dict2.keys():
      dict2[c] = 1
    else:
      dict2[c] += 1
  for c in s1:
    if c not in dict1.keys():
      dict1[c] = 1
    else:
      dict1[c] += 1
  
  for k in dict2.keys():
    if dict2[k] > dict1[k]:
      return False
  
  return True


def min_length_substring(s, t):
  # Write your code here
  # sliding window approach
  lptr = 0
  rptr = len(t)
  ans = len(s) + 1
  flag = True
  while lptr < len(s) - len(t) and flag:
    while (not str_contains(s[lptr:rptr], t) and rptr <= len(s)):
      # when this is false, increase rpter
      rptr += 1
    # not applicable anymore
    if rptr > len(s):
      flag = False
      continue
    # next narrow down the lptr
    while (str_contains(s[lptr:rptr], t)):
      lptr += 1
    print(lptr, " ", rptr)
    if rptr - lptr + 1 < ans:
      ans = rptr - lptr + 1
  
  if ans < len(s) + 1:
    return ans
  else:
    return -1
  



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
  s1 = "dcbefebce"
  t1 = "fd"
  expected_1 = 5
  output_1 = min_length_substring(s1, t1)
  check(expected_1, output_1)

  s2 = "bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf"
  t2 = "cbccfafebccdccebdd"
  expected_2 = -1
  output_2 = min_length_substring(s2, t2)
  check(expected_2, output_2)

  # Add your own test cases here
  