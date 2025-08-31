class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        used = set()
        n = len(hand)
        if n % groupSize != 0:
            return False
        
        def build(i):
            curr = hand[i]
            size = 1
            used.add(i)
            i += 1
            while i < n and size < groupSize:
                if hand[i] == curr + 1 and i not in used:
                    used.add(i)
                    curr = hand[i] 
                    size += 1
                elif hand[i] > curr + 1:
                    return False
                i += 1
            if size == groupSize:
                return True
            return False
        
        for i in range(n):
            if i not in used:
                if not build(i):
                    return False

        return len(used) == n

