class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right, left = len(numbers) - 1, 0
        
        while left <= right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]
            if sum < target:
                left += 1
            else:
                right -= 1