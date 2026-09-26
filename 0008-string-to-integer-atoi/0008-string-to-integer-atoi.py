class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1        # 2147483647
        INT_MIN = -2**31           # -2147483648

        i = 0
        n = len(s)

        # 1) Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # 2) If only spaces or empty
        if i == n:
            return 0

        # 3) Read optional sign
        sign = 1
        if s[i] == '+' or s[i] == '-':
            if s[i] == '-':
                sign = -1
            i += 1

        # 4) Read digits with overflow check
        res = 0
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')

            # Overflow check before multiplying
            if sign == 1:
                if res > INT_MAX // 10 or (res == INT_MAX // 10 and digit > INT_MAX % 10):
                    return INT_MAX
            else:  # sign == -1
                # For negative numbers allowed magnitude is 2147483648
                if res > INT_MAX // 10 or (res == INT_MAX // 10 and digit > 8):
                    return INT_MIN

            res = res * 10 + digit
            i += 1

        return sign * res