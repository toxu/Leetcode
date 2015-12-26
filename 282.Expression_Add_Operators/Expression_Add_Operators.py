class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        self.target = target
        result = []
        self.helper(num, 0, 0, "", result)
        return result
    
    def helper(self, num, current, previous, solution, result):
    	if num == "" and current == self.target:
    		result.append(solution)
    		return
    	else:
    		for i in range(1, len(num)+1):
    			current_string = num[0:i]
    			next_string = num[i:]
    			if len(current_string) > 1 and current_string[0] == '0':
    				return
    			if len(solution) == 0:
    				self.helper(next_string, int(current_string), int(current_string), current_string, result)
    			else:
    				self.helper(next_string, current+int(current_string), int(current_string), solution+"+"+current_string, result)
    				self.helper(next_string, current-int(current_string), -int(current_string), solution+"-"+current_string, result)
    				self.helper(next_string, current-previous+previous*int(current_string), previous*int(current_string), solution+"*"+current_string, result)

s = Solution()
print s.addOperators("123", 6)    				