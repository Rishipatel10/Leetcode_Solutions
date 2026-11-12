class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans = []
        for i in range(len(words)):
            word = words[i]
            s = ""
            for ch in word:
                if ch == separator:
                    if len(s) != 0:
                        ans.append(s)
                    s = ""
                    continue
                s += ch
            if len(s) != 0:
                ans.append(s)
        return ans