class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        new=[]

        for ch in s:
            if ch in vowels:
                new.append(ch)
        new=new[::-1]
        result=[]
        index=0

        for ch in s:
            if ch in vowels:
                result.append(new[index])
                index+=1
            else:
                result.append(ch)

        return "".join(result)


