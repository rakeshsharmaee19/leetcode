class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        for i in  range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=='0':
                    matrix[i][j]=-40000
                else:
                    matrix[i][j]=1
        n = len(matrix)
        m = len(matrix[0])
        gm = 0
        for i in range(n):
            temp = [0]*m
            for j in range(i, n):
                for k in range(m):
                    temp[k]+=matrix[j][k]
                cs = 0
                cm = 0
                for s in range(m):
                    cs = max(temp[s], cs+temp[s])
                    cm=max(cm, cs)
                gm=max(gm,cm)
        return gm
