class Solution(object):
    def calculate(self, s):
        s = s.replace(' ', '')
        stack = []
        ans = 0
        now = 0
        sign = 1

        for i in xrange(len(s)):
            if s[i].isdigit():
                now = now*10 + int(s[i])
                continue
            stack.append(sign * now)
            now = 0
            if s[i] == '+':
                sign = 1
            elif s[i] == '-':
                sign = -1
            elif s[i] == '(':
                if sign == 1:
                    stack.append('+')
                else:
                    stack.append('-')
                sign = 1
            elif s[i] == ')':
                tmp = 0
                while stack[-1] != '+' and stack[-1] != '-':
                    tmp += stack.pop()
                if stack[-1] == '-':
                    tmp = -tmp
                stack.pop() # pop + or - sign
                stack.append(tmp)

        if now != 0:
            stack.append(sign * now)
        while stack:
            ans += stack.pop()

        return ans

s = Solution()
print s.calculate('(1+1)')

