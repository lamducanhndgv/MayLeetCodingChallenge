class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums) # length of 'nums'
        d = collections.defaultdict(int) # create a defaultdict for counting appearence of element in 'nums'
        for num in nums:
            d[num] += 1
            if d[num] > n // 2:
                return num
