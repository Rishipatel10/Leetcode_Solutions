class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = {}
        for i in range(len(text)):
            if text[i] in count:
                count[text[i]] += 1
            else:
                count[text[i]] = 1
        b = count.get("b",0)
        a = count.get("a",0)
        l = count.get("l",0) // 2
        o = count.get("o",0) // 2
        n = count.get("n",0)
        return min (b,a,l,o,n)