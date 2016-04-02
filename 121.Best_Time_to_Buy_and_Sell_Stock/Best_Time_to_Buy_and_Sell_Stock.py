class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return -1
        diffs = []
        for i in range(1, len(prices)):
            diffs.append(prices[i]-prices[i-1])
        
        local_max, global_max = 0, 0
        for diff in diffs:
            local_max = max(local_max+diff, 0)
            global_max = max(global_max, local_max)

        return global_max
