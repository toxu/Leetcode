class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValid(s):
        	dic = {'(':1, ')':-1}
        	Sum = 0
        	for ch in s:
        		Sum += dic.get(ch, 0)
        		if Sum < 0:
        			return False
        	return Sum == 0
        queue = {s}
        res = []
        while True:
	        for candidate in queue:
	        	if isValid(candidate):
	        		res.append(candidate)
	        if res:
	        	return res
	        queue = {s[:i]+s[i+1:] for s in queue for i in range(len(s))}


       	# def isValid(s):
        #     a = 0
        #     for ch in s:
        #         a += {'(':1, ')':-1}.get(ch, 0)
        #         if a < 0:
        #             return False
        #     return a == 0
        # queue = {s}
        # while True:
        #     res = filter(isValid, queue)
        #     if res:
        #         return res
        #     queue = {s[:i]+s[i+1:] for s in queue for i in range(len(s))}
        # return res


