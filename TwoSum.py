# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].




# solution 

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dist = {}  # Initialize an empty dictionary to store numbers and their indices

        # Iterate over the list of numbers with their indices
        for i, num in enumerate(nums):
            compliment = target - num  # Calculate the required complement

            # Check if the complement is already in the dictionary
            if compliment in num_dist:
                # If found, return the indices of the complement and the current number
                return [num_dist[compliment], i]

            # If not found, store the current number and its index in the dictionary
            num_dist[num] = i

        return []  # If no solution is found, return an empty list


solution = Solution()
nums = [2, 7, 11, 15]
target = 9
result = solution.twoSum(nums, target)
print(result)  # Output: [0, 1]
