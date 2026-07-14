class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        answer=[1]*n

        prefix=1
        for i in range(n):
            answer[i]=prefix
            prefix=nums[i]*prefix

        suffix=1
        for i in range(n-1,-1,-1):
            answer[i]=answer[i]*suffix
            suffix=suffix*nums[i]
        return answer



















        # new=[]
        # mul=1

        # for i in range(len(nums)):
        #      mul=1
        #      for j in range((len(nums))):
        #         if i!=j:
        #     # while i < len(nums)-1:
        #          mul=nums[j]*mul
        #      new.append(mul)

        # nums[:]=new
        # return nums



        