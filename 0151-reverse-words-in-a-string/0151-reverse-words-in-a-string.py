class Solution:
    def reverseWords(self, s: str) -> str:
        temp = s.split()
        l = len(temp)
        rev=""
        while l>0:
            rev = rev + str(temp[l-1])
            l-=1
            if l!=0:
                rev = rev + " "

        return rev