# here the val is given and asked to remove the val element from the list .. so if we use a while statemnent and two pointer concept it will take more time and also its not efficiednt
# so we here are using a single poitner and also a for loop

# example

# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).


# solution

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0  # Initialize the index for the position of valid elements

        # Iterate through the entire list
        for i in range(len(nums)):
            # Check if the current element is not equal to the value to be removed
            if nums[i] != val:
                nums[index] = nums[i]  # Assign the valid element to the 'index' position
                index += 1  # Move to the next index for valid elements

        return index  # Return the count of valid elements


solution = Solution()
nums = [3, 2, 2, 3]
val = 3
length = solution.removeElement(nums, val)
print(length)  # Output: 2
print(nums[:length])  # Output: [2, 2]
