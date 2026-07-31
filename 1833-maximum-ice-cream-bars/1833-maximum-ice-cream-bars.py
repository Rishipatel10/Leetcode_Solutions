class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count = 0
        total = 0
        costs.sort()
        for i in range(len(costs)):
            total+=costs[i]
            if total > coins:
                break
            count+=1
        return count
