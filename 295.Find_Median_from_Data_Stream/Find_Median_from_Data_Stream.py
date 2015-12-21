import heapq

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.small_heap = []
        self.max_heap = []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if len(self.small_heap) == len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappushpop(self.small_heap, -num))
        else:
            heapq.heappush(self.small_heap, -heapq.heappushpop(self.max_heap, num))

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.small_heap) == len(self.max_heap):
            return float(self.max_heap[0] - self.small_heap[0]) / 2.0
        else:
            return float(self.max_heap[0])

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()
