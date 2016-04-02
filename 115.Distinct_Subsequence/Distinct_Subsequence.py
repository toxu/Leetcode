class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        len_s = len(s)
        len_t = len(t)
        dp = [[0 for i in range(len_s+1)] for j in range(len_t+1)]
        for i in range(len_s+1):
            dp[0][i] = 1
        for i in range(len_t+1):
            dp[i][0] = 0
        dp[0][0] = 1
        for i in range(1, len_t+1):
            for j in range(1, len_s+1):
                dp[i][j] = dp[i][j-1] if s[j-1] != t[i-1] else dp[i][j-1] + dp[i-1][j-1]
        return dp[len_t][len_s]


s = Solution()
print s.numDistinct('rabbbit', 'rabbit')
