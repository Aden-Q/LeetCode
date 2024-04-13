from collections import defaultdict

class Logger:

    def __init__(self):
        self.message_log = defaultdict(int)
        
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.message_log:
            self.message_log[message] = timestamp
            return True
        if timestamp >= self.message_log[message] + 10:
            self.message_log[message] = timestamp
            return True
        return False

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)