import heapq

class KthLargest(object):
    def __init__(self, k, nums):
        self.pool = nums
        self.k = k
        self.heap=[]
        for x in self.pool:
            if len(self.heap)<self.k:
                heapq.heappush(self.heap,x)
            else:
                if x>self.heap[0]:
                    heapq.heappop(self.heap)
                    heapq.heappush(self.heap,x)
                
                    
            
    def add(self, val):
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap,val)
        return self.heap[0]

    
