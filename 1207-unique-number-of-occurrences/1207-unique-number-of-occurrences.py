class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        count={}
        for num in arr:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        freq=set()
        # freq = set(count)it gives nums not values hash map  stores in way like key value pair we want value

        for value in count.values():
            freq.add(value)
        if len(count)==len(freq):
            return True
        else:
            return False


                


        