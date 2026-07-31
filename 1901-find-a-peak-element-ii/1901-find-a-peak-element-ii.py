class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        maxi = float('-inf')
        row = -1
        col = -1

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] > maxi:
                    maxi = mat[i][j]
                    row = i
                    col = j
                    
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if maxi == mat[i][j]:
                    return [i,j]
