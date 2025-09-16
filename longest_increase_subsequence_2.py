class SEG:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (2 * n)
    
    def update(self, index, val):
        index += self.n
        while index >= 1:
            self.tree[index] = max(self.tree[index], val)
            index>>=1

    def query(self, l, r):
        l += self.n
        r += self.n
        res = 0
        while l < r:
            if l & 1:
                res = max(res, self.tree[l])
                l += 1
            
            if r & 1:
                r -= 1
                res = max(res, self.tree[r])
            l>>=1
            r>>=1
        return res

class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        n, ans = max(nums), 1
        tree = SEG(n)
        for num in nums:
            num -= 1
            tree_val = tree.query(max(num-k, 0), num) + 1
            ans = max(tree_val, ans)
            tree.update(num, tree_val)
        return ans