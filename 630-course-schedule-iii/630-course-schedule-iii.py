from heapq import *
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        time = 0
        heap = []
        
        for i in sorted(courses, key = lambda x:x[1]):
            if i[0] <= i[1]:
                if i[0] + time <= i[1]:
                    heappush(heap, -i[0])
                    time += i[0]
                else:
                    if -heap[0] > i[0]:
                        time += heappop(heap)
                        time += i[0]
                        heappush(heap, -i[0])
        return len(heap)