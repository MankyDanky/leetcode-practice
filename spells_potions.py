class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(spells)
        m = len(potions)
        tagged = [(spells[i], i) for i in range(n)] 
        tagged.sort()
        potions.sort()
        pairs = [0] * n
        for i in range(n):
            spell, index = tagged[i]
            needed = success/spell
            p = bisect.bisect_left(potions, needed)
            pairs[index] = m - p
        return pairs