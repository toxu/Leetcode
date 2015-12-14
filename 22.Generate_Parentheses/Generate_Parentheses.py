class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        solution = ''
        result = []
        self.dfs(n, 0, solution, result)
        return result
    
    def dfs(self, n, pos, solution, result):
        if pos == 2*n:
            if self.isValid(n, solution):
                result.append(solution)
            return
        if self.isValid(n, solution):
            self.dfs(n, pos+1, solution + '(', result)
            self.dfs(n, pos+1, solution + ')', result)
        else:
            return
        
    def isValid(self, num, solution):
        left = []
        count = 0
        for i in range(len(solution)):
            if solution[i] == '(':
                left.append('(')
                count += 1
            else:
                if len(left) != 0:
                    left.pop()
                else:
                    return False
                
        return count <= num
        
        
            