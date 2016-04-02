#class Solution(object):
#    def canFinish(self, numCourses, prerequisites):
#        """
#        :type numCourses: int
#        :type prerequisites: List[List[int]]
#        :rtype: bool
#        """
#        count = [0 for i in range(numCourses)]
#        for pre in prerequisites:
#            count[pre[0]] += 1
#        print count
#        res = []
#        while True:
#            found = False
#            for i in range(numCourses):
#                if count[i] == 0 and i not in res:
#                    found = True
#                    res.append(i)
#                    for pre in prerequisites:
#                        if pre[1] == i:
#                            count[pre[0]] -= 1
#            print res, count
#            if len(res) == numCourses or max(count) == 0:
#                return True
#            if not found:
#                return False
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        ind = [[] for i in range(numCourses)]
        oud = [0] * n  
        for p in pres:
            oud[p[0]] += 1
            ind[p[1]].append(p[0])
        res = []
        for i in range(numCourses):
            if oud[i] == 0:
                res.append(i)
        k = 0
        while res:
            tmp = res.pop(0)
            k += 1
            for i in ind[tmp]:
                oud[i] -= 1
                if oud[i] == 0:
                    res.append(i)
        return k == numCourses
s = Solution()
print s.canFinish(4, [[3,0],[0,1]])
