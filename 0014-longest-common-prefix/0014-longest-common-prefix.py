class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        
        prefix = strs[0]
        
        
        for string in strs[1:]:
            while not string.startswith(prefix):
                prefix = prefix[:-1]  # Remove last character
                if not prefix:
                    return ""  # No common prefix found
        return prefix


solution = Solution()


strs1 = ["flower", "flow", "flight"]
print(solution.longestCommonPrefix(strs1))  # Output: "fl"


strs2 = ["dog", "racecar", "car"]
print(solution.longestCommonPrefix(strs2))  # Output: ""


strs3 = ["interview", "internet", "internal"]
print(solution.longestCommonPrefix(strs3))  # Output: "inte"

strs4 = ["single"]
print(solution.longestCommonPrefix(strs4))  # Output: "single"

strs5 = ["", "empty", "none"]
print(solution.longestCommonPrefix(strs5))  # Output: ""
