class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        str1 = [""] * len(s)
        for i in range(len(s)):
            str1[indices[i]] = s[i]
        return "".join(str1)