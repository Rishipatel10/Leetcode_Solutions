class Solution:
    def average(self, salary: List[int]) -> float:
        maxi = max(salary)
        mini = min(salary)
        sum = 0
        c = 0
        for i in salary:
            if i == maxi or i == mini:
                continue
            sum += i
            c += 1
        avg = sum / c
        return avg