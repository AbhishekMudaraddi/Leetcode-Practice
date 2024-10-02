

# Example 1:

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# solution 
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)  # Get the length of the input list
        if n == 0:     # Check for edge case: empty list
            return 0

        j = 1  # Initialize a pointer for the position of unique elements

        # Iterate through the list starting from the second element
        for i in range(1, n):
            # If the current element is different from the previous one
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]  # Assign the unique element to the 'j' index
                j += 1  # Increment the unique element index

        return j  # Return the length of the unique elements

solution = Solution()
nums = [1, 1, 2, 2, 3, 4]
length = solution.removeDuplicates(nums)
print(length)  # Output: 4
print(nums[:length])  # Output: [1, 2, 3, 4]
