class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        
        def rec(bits):

            if len(bits) == 1:
                return True
            
            if len(bits) == 2:
                if bits == "10":
                    return False
                return True
            pref = bits[0] + bits[1]
            if pref == "10" or pref == "11":
                return rec(bits[2:])
            return rec(bits[1:])
        return rec("".join(map(str, bits)))