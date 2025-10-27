class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        prev = 0
        for row in bank:
            lasers = row.count("1")
            if lasers == 0:
                continue
            res += prev * lasers
            prev = lasers
        return res