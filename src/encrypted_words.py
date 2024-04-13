import math
# Add any extra import statements you may need here


# Add any helper functions you may need here

def encrptUtils(s):
  # base case
  if len(s) <= 1:
    return s
  
  cur_s = ""
  if len(s) % 2 == 0:
    idx = (len(s) - 1) // 2
  else:
    idx = len(s) // 2
  
  return s[idx] + encrptUtils(s[0:idx]) + encrptUtils(s[idx+1:])
  


def findEncryptedWord(s):
  # Write your code here
  
  return encrptUtils(s)
  











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
  s1 = "abc"
  expected_1 = "bac"
  output_1 = findEncryptedWord(s1)
  check(expected_1, output_1)

  s2 = "abcd"
  expected_2 = "bacd"
  output_2 = findEncryptedWord(s2)
  check(expected_2, output_2)

  # Add your own test cases here
  s3 = "a"
  expected_3 = "a"
  output_3 = findEncryptedWord(s3)
  check(expected_3, output_3)
  