class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        dictionary.sort(key=len)
        
        words = sentence.split()
        for i in range(len(words)):
            for j in dictionary:
                if words[i].startswith(j):
                    words[i] = j
                    break
        return ' '.join(words)