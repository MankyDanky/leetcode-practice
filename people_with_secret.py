class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        knowers = set()
        knowers.add(0)
        knowers.add(firstPerson)
        meetings.sort(key = lambda x: x[2])

        rank = [1] * n
        known = [False] * n
        par = [1] * n
        timer = 1
        time = [0] * n

        def find(node):
            if time[node] != timer:
                par[node] = node
                time[node] = timer
                rank[node] = 1
                known[node] = False
                return node
            if par[node] == node:
                return node
            res = find(par[node])
            par[node] = res
            return res
        
        def unite(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                par[p2] = p1
                if known[p2]:
                    known[p1] = True
            else:
                rank[p2] += rank[p1]
                par[p1] = p2
                if known[p1]:
                    known[p2] = True
            return True

        def reset():
            nonlocal timer
            timer+=1

        i = 0
        s = len(meetings)
        while i < s:
            j = i
            reset()
            while j < s and meetings[i][2] == meetings[j][2]:
                j += 1

            for k in range(i, j):
                m = meetings[k]
                unite(m[0], m[1])
                if m[0] in knowers or m[1] in knowers:
                    known[find(m[0])] = True
            
            for k in range(i, j):
                m = meetings[k]
                if known[find(m[0])]:
                    knowers.add(m[0])
                    knowers.add(m[1])
            i = j
            
        return list(knowers)