class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        index = 0
        operators = ['+', '-', '*', '/']
        num_stack = []
        op_stack = []
        while index < len(s):
            if s[index] == ' ':
                index += 1
                continue
            if s[index] in operators:
                if s[index] == '+' or s[index] == '-':
                    op_stack.append(s[index])
                    index += 1
                else:
                    index += 1
                    pre = num_stack[-1]
                    val, pos = self.getNum(s, index)
                    nex = val
                    if s[index-1] == '*':
                        num_stack[-1] = pre*nex
                    else:
                        num_stack[-1] = pre/nex
                    index = pos
            else:
                val, pos = self.getNum(s, index)
                num = int(s[index:pos])
                num_stack.append(num)
                index = pos
        if len(op_stack) == 0:
            return num_stack[0]
        val = 0
        start = 0
        for op in op_stack:
            if op == '+':
                val = num_stack[start] + num_stack[start + 1]
                num_stack[start+1] = val
            else:
                val = num_stack[start] - num_stack[start + 1]
                num_stack[start+1] = val
            start += 1
        return num_stack[-1]

    def getNum(self, s, index):
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        num = 0
        start = index
        while index < len(s):
            if s[index] == ' ':
                index += 1
                start += 1
            else:
                break

        end = index
        while index < len(s):
            if s[index] == ' ':
                end += 1
                break
            elif s[index] in nums:
                index += 1
                end += 1
            else:
                break
        return int(s[start:end]), end

s = Solution()
print s.calculate('1+1+1')
