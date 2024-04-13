class Solution:
    def myAtoi(self, s: str) -> int:
        # trim leading zero in the digit string, remove other characters
        s_temp = s.lstrip()
        if len(s_temp) == 0:
            return 0
        elif s_temp[0] != '+' and s_temp[0] != '-' and not s_temp[0].isdigit():
            return 0
        # check the sign if it exists
        sign = 1
        if  s_temp[0] == '-':
            sign = -1
            s_temp = s_temp[1:]
        elif s_temp[0] == '+':
            sign = 1
            s_temp = s_temp[1:]
        # trim leading 0
        s_temp = s_temp.lstrip('0')
        # find the end index
        end_idx = 0
        for i in range(len(s_temp)):
            if s_temp[i].isdigit():
                end_idx += 1
            else:
                break
        s_temp = s_temp[:end_idx]
        if len(s_temp) == 0:
            return 0
        # check whether the number is within range
        int_max_str = str(2**31 - 1)
        int_min_str = str(2**31)
        if len(s_temp) > len(int_max_str) and sign == 1:
            return 2**31 - 1
        elif len(s_temp) == len(int_max_str) and sign == 1 and s_temp > int_max_str:
            return 2**31 - 1
        elif len(s_temp) > len(int_min_str) and sign == -1:
            return -(2**31-1) - 1
        elif (len(s_temp) == len(int_max_str) and sign == -1 and s_temp > int_min_str):
            return -(2**31-1) - 1
        else:
            return int(s_temp) * sign


if __name__ == '__main__':
  s = "2147483646"
  test = Solution()
  print(test.myAtoi(s))