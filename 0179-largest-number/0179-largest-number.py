class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        store = [str(num) for num in nums]
        from functools import cmp_to_key
        store.sort(key=cmp_to_key(lambda a, b: -1 if a+b > b+a else 1))
    
        if store[0] == "0":
            return "0"
        
        ans = "".join(store)
        
        return ans