# class Solution(object):
#     def longestValidParentheses(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         def isValid(s):
#             dic = {'(':1, ')':-1}
#             Sum = 0
#             for i in s:
#                 Sum += dic.get(i, 0)
#                 if Sum < 0:
#                     return False
#             return Sum == 0
#
#         def helper(s, res):
#             if not s:
#                 res.append(0)
#                 return
#             if isValid(s):
#                 res.append(len(s))
#                 return
#             for i in range(len(s)):
#                 helper(s[:i]+s[i+1:], res)
#             return
#
#         res = []
#         helper(s, res)
#         return max(res)
#
#
# class Solution(object):
#     def longestValidParentheses(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         # use 1D DP
#         # dp[i] records the longestValidParenthese EXACTLY ENDING at s[i]
#         dp = [0 for x in xrange(len(s))]
#         max_to_now = 0
#         for i in xrange(1,len(s)):
#             if s[i] == ')':
#                 # case 1: ()()
#                 if s[i-1] == '(':
#                     # add nearest parentheses pairs + 2
#                     dp[i] = dp[i-2] + 2
#                 # case 2: (())
#                 # i-dp[i-1]-1 is the index of last "(" not paired until this ")"
#                 elif i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
#                     if dp[i-1] > 0: # content within current matching pair is valid
#                     # add nearest parentheses pairs + 2 + parentheses before last "("
#                         dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
#                     else:
#                     # otherwise is 0
#                         dp[i] = 0
#                 max_to_now = max(max_to_now, dp[i])
#         return max_to_now

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0 for i in range(len(s))]
        max_to_now = 0
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = dp[i-2] + 2
                elif i - dp[i-1] -1 >= 0 and s[i-dp[i-1]-1] == '(':
                    if dp[i-1] > 0:
                        dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
                    else:
                        dp[i] = 0
            max_to_now = max(max_to_now, dp[i])
        return max_to_now


s = Solution()
print s.longestValidParentheses('()(()))))')
