class Solution:
    def countMentions(self, n: int, events: List[List[str]]) -> List[int]:
        offline = deque([])
        online = set()
        for i in range(n):
            online.add(i)
        times = [0] * n
        events.sort(key=lambda x: (int(x[1]), 1 if x[0] == "MESSAGE" else 0))
        print(events)
        for event in events:
            t = int(event[1])
            while (offline and offline[0][0] <= t):
                t2, i = offline.popleft()
                online.add(i)
            
            if (event[0] == "MESSAGE"):
                if event[2] == "ALL":
                    for i in range(n):
                        times[i] += 1
                elif event[2] == "HERE":
                    for i in online:
                        times[i] += 1
                else:
                    for i in event[2].split():
                        j = int(i[2:])
                        times[j] += 1
            else:
                i = int(event[2])
                online.remove(i)
                offline.append((t + 60, i))
        return times
