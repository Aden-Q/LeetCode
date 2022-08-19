class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        
        for log in logs:
            # retrieve the first token after the identifier
            if log.split()[1].isalpha():
                # is a letter log
                log_split = log.split()
                letter_logs.append((log_split[0], log_split[1:]))
            else:
                digit_logs.append(log)
                
        # Sort lexicographically all letter logs
        letter_logs.sort(key = lambda x : (x[1], x[0]))
        
        res = []
        for log in letter_logs:
            res.append("%s %s" % (log[0], ' '.join(log[1])))
        
        for log in digit_logs:
            res.append(log)
            
        return res