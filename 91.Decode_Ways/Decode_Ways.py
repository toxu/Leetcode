class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        if l == 0:
            return 0
        dp = [0 for i in range(l+1)]
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1
        for i in range(2, l+1):
            if int(s[i-2:i]) >= 10 and int(s[i-2:i]) <= 26:
                if(s[i-1] == '0'):
                    dp[i] = dp[i-2]
                else:
                    dp[i] = dp[i-1] + dp[i-2]
            else:
                if(s[i-1] == '0'):
                    dp[i] = 0
                else:
                    dp[i] = dp[i-1]
        return dp[l]

s = Solution()
print s.numDecodings('100')
