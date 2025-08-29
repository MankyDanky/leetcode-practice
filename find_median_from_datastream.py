class MedianFinder:

    def __init__(self):
        self.largeHeap = []
        self.smallHeap = []

    def addNum(self, num: int) -> None:
        if not self.smallHeap and not self.largeHeap:
            heapq.heappush(self.smallHeap, -num)
        elif not self.largeHeap:
            if num > -self.smallHeap[0]:
                heapq.heappush(self.largeHeap, num)
            else:
                heapq.heappush(self.largeHeap, -heapq.heappushpop(self.smallHeap, -num))
        elif not self.smallHeap:
            if num < self.largeHeap[0]:
                heapq.heappush(self.smallHeap, -num)
            else:
                heapq.heappush(self.smallHeap, -heapq.heappushpop(self.largeHeap, num))
        else:
            if num > -self.smallHeap[0]:
                heapq.heappush(self.largeHeap, num)
            else:
                heapq.heappush(self.smallHeap, -num)

            if len(self.smallHeap) > len(self.largeHeap) + 1:
                heapq.heappush(self.largeHeap, -heapq.heappop(self.smallHeap))
            elif len(self.largeHeap) > len(self.smallHeap) + 1:
                heapq.heappush(self.smallHeap, -heapq.heappop(self.largeHeap))

    def findMedian(self) -> float:
        print(self.smallHeap, self.largeHeap)
        if len(self.smallHeap) > len(self.largeHeap):
            return -self.smallHeap[0]
        elif len(self.largeHeap) > len(self.smallHeap):
            return self.largeHeap[0]
        else:
            return (-self.smallHeap[0] + self.largeHeap[0])/2
        