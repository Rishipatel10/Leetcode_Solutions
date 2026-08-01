class Solution:
    def isPalindrome(self, s: str) -> bool:
        str1=""
        str2=""
        for i in s:
            if i.isalnum():
                str1+=i

        str2=str1[::-1]
        return str1.lower() == str2.lower()
