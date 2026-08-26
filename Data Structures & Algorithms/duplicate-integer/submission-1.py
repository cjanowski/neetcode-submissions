class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Initialize hash set
        seen = set()
        # For each number
        # If already in set return True
        for num in nums:
            if num in seen:
                return True
        # If not in set, add to set
            seen.add(num)
        # If no duplicates return False
        return False
