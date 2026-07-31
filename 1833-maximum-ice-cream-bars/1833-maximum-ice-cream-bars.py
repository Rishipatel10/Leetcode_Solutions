class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count = 0
        sum = 0
        costs.sort()
        for i in range(len(costs)):
            sum+=costs[i]
            count+=1
            if sum > coins:
                sum-=costs[i]
                count-=1
        return count
