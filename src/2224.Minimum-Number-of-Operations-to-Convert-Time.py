class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current = current.split(':')
        correct = correct.split(':')
        current_hour, current_minute = int(current[0]), int(current[1])
        correct_hour, correct_minute = int(correct[0]), int(correct[1])
        current_time = current_hour * 60 + current_minute
        correct_time = correct_hour * 60 + correct_minute
        
        steps = 0
        # Greedy
        while correct_time - current_time >= 60:
            correct_time -= 60
            steps += 1

        while correct_time - current_time >= 15:
            correct_time -= 15
            steps += 1
            
        while correct_time - current_time >= 5:
            correct_time -= 5
            steps += 1
            
        while correct_time - current_time >= 1:
            correct_time -= 1
            steps += 1
        
        return steps