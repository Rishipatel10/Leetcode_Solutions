class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i][-1] > words[j][-1]:
                    words[i], words[j] = words[j], words[i]
        ans = []
        for word in words:
            ans.append(word[:-1])
        return " ".join(ans)