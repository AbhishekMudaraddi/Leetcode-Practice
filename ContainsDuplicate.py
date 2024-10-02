# To determine if an array contains duplicates and return True if it does and False if it doesn't, you can utilize a set to keep track of the unique elements.
# Example 
# Input: nums = [1,2,3,1]
# Output: true
# Explanation: The element 1 occurs at the indices 0 and 3.

# Solution 


from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set() #set to hold the values that are seen 

        for num in nums:
            if num in seen:
                return True  # Duplicate found
            seen.add(num)

        return False  # No duplicates found

# Example usage:
solution = Solution()
result = solution.containsDuplicate([3, 3, 4, 5])  # Using duplicates
print(result)  # Output: True


