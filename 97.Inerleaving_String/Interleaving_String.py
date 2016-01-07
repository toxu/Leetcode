# class Solution(object):
#     def isInterleave(self, s1, s2, s3):
#         """
#         :type s1: str
#         :type s2: str
#         :type s3: str
#         :rtype: bool
#         """
#         def helper(s1, s2, s3, part1, part2):
#             if not s3:
#                 return s1 == part1 and s2 == part2
#             else:
#             	i = 0
#                 return helper(s1,s2,s3[:i]+s3[i+1:], part1+s3[i], part2) or helper(s1,s2,s3[:i]+s3[i+1:], part1, part2+s3[i])

#         if len(s1) + len(s2) != len(s3):
#             return False
#         return helper(s1,s2,s3,"","")


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        
s= Solution()
print s.isInterleave('aabcc', 'dbbca', 'aadbbcbcac')
