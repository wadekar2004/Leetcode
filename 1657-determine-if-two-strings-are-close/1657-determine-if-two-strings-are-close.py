# 1. Length same?
#         ↓
# 2. Count frequency (Hash Map)
#         ↓
# 3. Same unique characters? (Hash Set)
#         ↓
# 4. Same frequency counts? (Sort values)
#         ↓
# 5. Return True
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        if len(word1) !=len(word2):
            return False

        count1={}
        count2={}

        for ch in word1:
            if ch in count1:
                count1[ch]+=1
            else:
                count1[ch]=1
        for ch in word2:
            if ch in count2:
                count2[ch]+=1
            else:
                count2[ch]=1
        if set(count1.keys())!=set(count2.keys()):
            return False
        if sorted(count1.values()) !=sorted(count2.values()):
            return False
        return True
    
        
        