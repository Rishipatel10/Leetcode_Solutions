class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        maxi = mat[0][0]
        row = 0
        col = 0

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
