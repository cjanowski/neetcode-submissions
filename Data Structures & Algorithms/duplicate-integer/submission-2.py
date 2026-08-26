class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # store seen numbers
        seen = set()
        for num in nums:
            if num in seen:
                # duplicate was found
                return True
            else:
                seen.add(num)
        return False