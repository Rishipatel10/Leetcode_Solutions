class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        mid = n//2
        str1 = ""
        for i in range(mid):
            str1 += s[i].lower()
        str2 = ""
        for i in range(mid,n):
            str2 += s[i].lower()

        c1 = 0
        c2 = 0
        for i in range(mid):
            if str1[i] == 'a' or str1[i] == 'e' or str1[i] == 'i' or str1[i] == 'o' or  str1[i] == 'u':
                c1 += 1
            if str2[i] == 'a' or str2[i] == 'e' or str2[i] == 'i' or str2[i] == 'o' or  str2[i] == 'u':
                c2 += 1
        return c1 == c2
