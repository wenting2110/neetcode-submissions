class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = {}
        for idx, item in enumerate(points):
            dist = item[0] ** 2 + item[1] ** 2
            dists[idx] = dist
        
        min_heap = [(val, key) for key, val in dists.items()]  # key == idx
        heapq.heapify(min_heap)  # 用 key 去排 heap

        res = []
        for i in range(k):
            small = heapq.heappop(min_heap)  # (dist, idx)
            res.append(points[small[1]])
        
        return res