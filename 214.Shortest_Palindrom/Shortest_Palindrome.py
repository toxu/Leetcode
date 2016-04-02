class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def isPalindrome(s):
            reverse = s[::-1]
            return s == reverse

        mid = len(s) / 2 - 1
        for i in range(mid, -1, -1):
            left = len(s[:i])
            right = len(s[i+1:])
            if not isPalindrome(s[:i]+s[i:i+left+1]):
                continue
            else:
                insert = s[i+left+1:]
                return insert[::-1] + s
