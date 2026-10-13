class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        ans = 0
        while mainTank >= 5:
            ans += 50
            mainTank -= 5
            if additionalTank > 0:
                mainTank += 1
                additionalTank -= 1
        ans += mainTank * 10
        return ans