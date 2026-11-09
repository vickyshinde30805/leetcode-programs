
import heapq
from sortedcontainers import SortedList
from typing import List

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:

        available = SortedList(range(k))
        busy = []
        count = [0] * k

        for i in range(len(arrival)):
            time = arrival[i]

            # Release servers that have completed their requests
            while busy and busy[0][0] <= time:
                end_time, server = heapq.heappop(busy)
                available.add(server)

            if not available:
                continue

            # Find the first available server >= i % k
            start = i % k
            idx = available.bisect_left(start)

            if idx == len(available):
                idx = 0

            server = available.pop(idx)

            # Assign request
            count[server] += 1
            heapq.heappush(busy, (time + load[i], server))

        # Find busiest servers
        maximum = max(count)

        return [i for i in range(k) if count[i] == maximum]
