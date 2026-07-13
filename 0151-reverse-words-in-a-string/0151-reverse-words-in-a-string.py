class Solution:
    def reverseWords(self, s: str) -> str:
        # # stat=int(s)
        # reversed=""
        # words=s.split()

        # for word in words:
        #          reversed=word + " " +reversed

        # return reversed.strip()

        return " ".join(s.split()[::-1])

        