class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=0
        new=[]

        for n in nums:
            if n!=0:
                new.append(n)
            else:
                count+=1

        for i in range(count):
            new.append(0)

        nums[:]=new

        # return new


        