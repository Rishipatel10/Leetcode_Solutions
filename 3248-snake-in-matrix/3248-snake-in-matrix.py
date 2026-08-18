class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        r = 0
        c = 0
        for i in range(len(commands)):
            if commands[i] == "UP":
                r -= 1 
            elif commands[i] == "DOWN":
                r += 1
            elif commands[i] == "LEFT":
                c -= 1
            else:
                c += 1
        return (r*n + c)