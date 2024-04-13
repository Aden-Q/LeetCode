class Solution:
    def reorderSpaces(self, text: str) -> str:
        words_list = text.split()
        num_words = len(words_list)
        number_space = len(text) - sum(len(word) for word in words_list)
        # We need to place the spaces between those num_words - 1 gap
        # number_space // num_words spaces per gap, and the reamining in the end
        res = []
        if num_words > 1:
            spaces_per_gap = number_space // (num_words - 1)
        else:
            spaces_per_gap = 0
        for idx, word in enumerate(words_list):
            res.append(word)
            if idx != len(words_list) - 1:
                res.append(' ' * spaces_per_gap)
        res.append(' ' * (number_space - spaces_per_gap * (num_words - 1)) )
        return ''.join(res)