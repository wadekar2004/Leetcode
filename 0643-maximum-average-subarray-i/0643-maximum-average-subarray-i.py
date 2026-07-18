class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum=0
        for i in range(k):
            sum+=nums[i]

        max_sum=sum
        for i in range(k,len(nums)):
            sum=sum-nums[i-k]+nums[i]

            if sum > max_sum:
             max_sum=sum
      
        return max_sum/k

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # max_avg=float('-inf')


        # for i in range(len(nums)-k+1):
        #     sum=0
        #     for j in range(k):
        #         sum+=nums[i+j]
        #     avg=sum/k

        #     if avg > max_avg:
        #      max_avg=avg
      
        # return max_avg

        