class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        children = defaultdict(list)

        for u, v in hierarchy:
            children[u].append(v)
        
        def dfs(node):
            resBought = [0] * (budget+1)
            resSkip = [0] * (budget+1)

            boughtDp = [0] * (budget+1) # Bought parent
            skipDp = [0] * (budget+1) # Skipped parent
            
            for v in children[node]:
                b, s = dfs(v)
                cost = present[v-1]

                for bud in range(budget, -1, -1):
                    for rem in range(0, bud+1):
                        skipDp[bud] = max(skipDp[bud], skipDp[bud-rem] + s[rem])
                
                cost//=2
                for bud in range(budget, -1, -1):
                    for rem in range(0, bud+1):
                        boughtDp[bud] = max(boughtDp[bud], boughtDp[bud - rem] + b[rem])
                

            cost = present[node-1]
            price = future[node-1]

            for i in range(budget+1):
                resBought[i] = skipDp[i]
                resSkip[i] = skipDp[i]
                if i >= cost:
                    resSkip[i] = max(resSkip[i], price - cost + boughtDp[i-cost])
                if i >= cost//2:
                    resBought[i] = max(resBought[i], price - cost//2 + boughtDp[i - (cost//2)])
                

            return resBought, resSkip
        b, s = dfs(1)

        return max(s)



            