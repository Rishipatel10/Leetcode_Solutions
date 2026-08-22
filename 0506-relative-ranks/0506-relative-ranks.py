class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        arr1 = sorted(score, reverse = True)
        rank = {}
        for i in range(len(arr1)):
            if i == 0:
                rank[arr1[i]] = "Gold Medal"
            elif i == 1:
                rank[arr1[i]] = "Silver Medal"
            elif i == 2:
                rank[arr1[i]] = "Bronze Medal"
            else:
                rank[arr1[i]] = str(i+1)
        ans = []
        for j in score:
            ans.append(rank[j])
        return ans