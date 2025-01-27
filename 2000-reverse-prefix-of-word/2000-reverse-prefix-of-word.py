class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        n = word.find(ch)
        rev = ""
        if ch in word:
            for i in range(n,-1,-1):
                rev = rev + word[i]
            rev = rev + word[n+1:]
            return rev
        else:
            return word