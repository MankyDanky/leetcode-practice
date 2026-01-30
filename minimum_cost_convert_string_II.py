class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        INF = 1e9
        dist = [[INF] * 26 for _ in range(26)]
        for i in range(26):
            dist[i][i] = 0

        for i in range(len(original)):
            dist[ord(original[i]) - ord('a')][ord(changed[i]) - ord('a')] = min(dist[ord(original[i]) - ord('a')][ord(changed[i]) - ord('a')], cost[i])
        
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


        res = 0
        for i in range(len(source)):
            if dist[ord(source[i]) - ord('a')][ord(target[i]) - ord('a')] == INF:
                return -1
            res += dist[ord(source[i]) - ord('a')][ord(target[i]) - ord('a')]
        return res