class StringIterator:

    def __init__(self, compressedString: str):
        self.ss = compressedString
        # a pointer pointing to the current character to be iterated
        self.char_ptr = 0
        # the remaining count of the current character
        self.next_char_ptr = 1
        self.cnt = 0
        while self.next_char_ptr < len(compressedString) and compressedString[self.next_char_ptr].isdigit():
            self.cnt = self.cnt * 10 + int(compressedString[self.next_char_ptr])
            self.next_char_ptr += 1

    def next(self) -> str:
        if not self.hasNext():
            return " "
        
        self.cnt -= 1
        return self.ss[self.char_ptr]

    def hasNext(self) -> bool:
        if self.cnt > 0:
            return True
        
        self.char_ptr = self.next_char_ptr
        if self.char_ptr >= len(self.ss):
            return False

        self.next_char_ptr = self.char_ptr + 1
        while self.next_char_ptr < len(self.ss) and self.ss[self.next_char_ptr].isdigit():
            self.cnt = self.cnt * 10 + int(self.ss[self.next_char_ptr])
            self.next_char_ptr += 1
        
        return True

# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()