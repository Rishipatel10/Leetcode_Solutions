class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        c = 0
        for i in range(len(s)):
            for j in range(i,len(words)):
                word = words[j]
                for k in range(len(word)):
                    if s[i] == word[k]:
                        c+=1
                    break
                break
        print(c)
        return c == len(words) and c == len(s)