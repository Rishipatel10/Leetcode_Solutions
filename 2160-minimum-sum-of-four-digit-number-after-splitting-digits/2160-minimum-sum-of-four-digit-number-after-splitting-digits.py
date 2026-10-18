class Solution:
    def minimumSum(self, num: int) -> int:
        arr = []
        while num:
            d = num % 10
            arr.append(d)
            num //= 10
        arr.sort()
        ans1 = ""
        ans2 = ""
        ans1 = str(arr[0]) + str(arr[len(arr)-1])
        ans2 = str(arr[1]) + str(arr[len(arr)-2])
        return int(ans1) + int(ans2)