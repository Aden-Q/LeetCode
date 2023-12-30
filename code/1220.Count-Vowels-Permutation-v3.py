class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = 10 ** 9 + 7
        # counting dp
        # we are going to build a string of length n
        # the current character is affected by the following characters
        # idx: the current idx of the string we are considering
        # prev_char: the previous character used to build the string
        # returns the number of ways to build a string with all the constraints ending at some idx
        # iterate from left to right so that we know the previous character to build the current one
        # this way we can quickly index into the dp array
        vowel_index = {vowel: idx for idx, vowel in enumerate('aeiou ')}

        prev_row = [1] * 6
        curr_row = [0] * 6
        for row in reversed(range(n)):
            for vowel in 'aeiou ':
                if vowel == 'a':
                    for c in 'e':
                        curr_row[vowel_index[vowel]] = (curr_row[vowel_index[vowel]] + prev_row[vowel_index[c]]) % mod
                elif vowel == 'e':
                    for c in 'ai':
                        curr_row[vowel_index[vowel]] = (curr_row[vowel_index[vowel]] + prev_row[vowel_index[c]]) % mod
                elif vowel == 'i':
                    for c in 'aeou':
                        curr_row[vowel_index[vowel]] = (curr_row[vowel_index[vowel]] + prev_row[vowel_index[c]]) % mod
                elif vowel == 'o':
                    for c in 'iu':
                        curr_row[vowel_index[vowel]] = (curr_row[vowel_index[vowel]] + prev_row[vowel_index[c]]) % mod
                elif vowel == 'u':
                    for c in 'a':
                        curr_row[vowel_index[vowel]] = (curr_row[vowel_index[vowel]] + prev_row[vowel_index[c]]) % mod
                else:
                    for c in 'aeiou':
                        curr_row[vowel_index[vowel]] = (curr_row[vowel_index[vowel]] + prev_row[vowel_index[c]]) % mod
            prev_row, curr_row = curr_row, prev_row
            for i in range(6):
                curr_row[i] = 0
        # we want to start building from index 0 and the previous used character is empty, indicating nothing used before
        # so we can choose any character to be the first one
        return prev_row[vowel_index[' ']]