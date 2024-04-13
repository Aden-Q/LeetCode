class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        if password == password.upper():
            return False
        if password == password.lower():
            return False
        cnt = 0
        for c in password:
            if c in '0123456789':
                cnt += 1
        if cnt == 0:
            return False
        cnt = 0
        for c in password:
            if c in "!@#$%^&*()-+":
                cnt += 1
        if cnt == 0:
            return False
        for i in range(1, len(password)):
            if password[i] == password[i-1]:
                return False
        return True