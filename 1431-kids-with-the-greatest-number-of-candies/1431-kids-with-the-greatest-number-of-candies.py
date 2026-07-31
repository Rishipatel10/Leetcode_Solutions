class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi = 0
        for i in candies:
            maxi = max(maxi,i)
        ans = []
        for i in candies:
            if i+extraCandies >= maxi:
                ans.append(True)
            else:
                ans.append(False)
        return ans