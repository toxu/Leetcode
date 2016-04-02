class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        nodes = preorder.split(',')
        if len(nodes) > 1 and nodes[0] == '#':
            return False
        if len(nodes) == 1 and nodes[0] == '#':
            return True
        stack = []
        for i in range(len(nodes)):
            if nodes[i] == '#':
                stack[-1] -= 1
                while True:
                    if stack[-1] < 0:
                        return False
                    if stack[-1] == 0:
                        stack.pop()
                        if len(stack) == 0 and i == len(nodes)-1:
                            return True
                        elif len(stack) == 0:
                            return False
                        stack[-1] -= 1
                    if stack[-1] > 0:
                        break
            else:
                stack.append(2)
        return len(stack) == 0

s = Solution()
print s.isValidSerialization("9,")
