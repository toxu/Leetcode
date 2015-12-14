class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)
        start = end = max_len = 0
        dic = {}
        for i, v in enumerate(s):
        	if v not in dic:
        		dic[v] = i
        	else:
        		start = dic[v] + 1
        		dic[v] = i
        		dic = {k:v for k,v in dic.items() if v >= start}
        	end += 1
        	max_len = max(max_len, end - start)
        return max_len

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        start = end = 0
        max_len = 0
        while end < len(s):
        	if s[end] not in dic:
        		dic[s[end]] = end
        		end += 1
        	else:
        		max_len = max(max_len, end-start)
        		start = end = dic[s[end]] + 1
        		dic = {}
        max_len = max(max_len, end-start)
        return max_len
