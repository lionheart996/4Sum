from typing import List


class Solution:
        def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
            nums.sort()  # Sort the array to handle duplicates easily and facilitate two-pointer technique
            quadruplets = []
            n = len(nums)

            for i in range(n):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue  # Skip duplicates
                for j in range(i + 1, n):
                    if j > i + 1 and nums[j] == nums[j - 1]:
                        continue  # Skip duplicates

                    left, right = j + 1, n - 1
                    while left < right:
                        total = nums[i] + nums[j] + nums[left] + nums[right]
                        if total == target:
                            quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                            while left < right and nums[left] == nums[left + 1]:
                                left += 1  # Skip duplicates
                            while left < right and nums[right] == nums[right - 1]:
                                right -= 1  # Skip duplicates
                            left += 1
                            right -= 1
                        elif total < target:
                            left += 1
                        else:
                            right -= 1

            return quadruplets

nums = [1,0,-1,0,-2,2]
nums_list = Solution().fourSum(nums, 0)
print(nums_list)
