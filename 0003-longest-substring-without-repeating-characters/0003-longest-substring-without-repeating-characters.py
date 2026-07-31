class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set1 = set()
        l = 0
        maxi = 0 
        for char in range(len(s)):
            while s[char] in set1:
                set1.remove(s[l])
                l+=1

            set1.add(s[char])
            maxi = max(maxi,char-l+1)

        return maxi
