class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        seen = set()
        for num in nums:
            if num in seen:
                return True # Duplicate number found
            else:
                seen.add(num) # Non-Duplicate number added in the list.
        return False


obj = Solution()

Duplicate1 = obj.hasDuplicate([1, 2, 3, 3])
print(Duplicate1)

Duplicate2 = obj.hasDuplicate([1, 2, 3, 4])
print(Duplicate2)
