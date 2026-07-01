class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newarr = [0]*(2*len(nums))

        for i in range(len(nums)):
            newarr[i]=newarr[i+len(nums)]=nums[i]
        return newarr
        