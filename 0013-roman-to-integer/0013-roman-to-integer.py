class Solution:
    def romanToInt(self, s):
        # Dictionary to map Roman symbols to values
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        # Loop through each character from right to left
        for char in reversed(s):
            value = roman_map[char]
            
            if value < prev_value:
                total -= value   # Subtract if smaller value before larger
            else:
                total += value   # Otherwise, add
            prev_value = value  # Update previous value
        
        return total
