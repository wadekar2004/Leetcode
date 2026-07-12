class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count=0

        for i in range(len(flowerbed)):
             if i==0:
                left=0
             else:
                left=flowerbed[i-1]   

             current=flowerbed[i]

             if i==len(flowerbed)-1:
                right=0
             else:
                right=flowerbed[i+1]
     
             if left==0 and current==0 and right==0:
               flowerbed[i]=1
               count+=1
        return count>=n


        
        