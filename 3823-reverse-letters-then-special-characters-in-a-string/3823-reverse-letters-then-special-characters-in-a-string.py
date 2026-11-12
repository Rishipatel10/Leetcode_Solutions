
class Solution:
    def reverseByType(self, s: str) -> str:
        s = list(s)
        l = 0
        r = len(s) - 1

        while l < r:
            if 'a' <= s[l] <= 'z' and 'a' <= s[r] <= 'z':
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

            elif not ('a' <= s[l] <= 'z'):
                l += 1

            else:
                r -= 1

        l = 0
        r = len(s) - 1
        while l < r:
            if not ('a' <= s[l] <= 'z') and not ('a' <= s[r] <= 'z'):
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

            elif 'a' <= s[l] <= 'z':
                l += 1

            else:
                r -= 1

        return "".join(s)
