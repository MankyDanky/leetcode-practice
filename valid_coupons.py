class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        valid_coupons = []
        n = len(code)
        valid = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_")
        categories = set(["restaurant", "pharmacy", "grocery", "electronics"])
        for i in range(n):
            if not isActive[i]:
                continue

            if businessLine[i] not in categories:
                continue

            if code[i] == "":
                continue
            
            valid_code = True
            for c in code[i]:
                if c not in valid:
                    valid_code = False
                    break
                    
            if not valid_code:
                continue
            
            valid_coupons.append((businessLine[i], code[i]))
        
        res = []
        valid_coupons.sort()
        for l, c in valid_coupons:
            res.append(c)
        return res
            
