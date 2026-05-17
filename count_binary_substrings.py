class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count1 = 1 if s[0] == '1' else 0
        count0 = 1 if s[0] == '0' else 0

        res = 0
        for i in range(1, len(s)):
            c = s[i]
            if c == '0':
                if s[i-1] == '1' and count0 != 0:
                    count0 = 1
                else:
                    count0 += 1
                if count1 >= count0:
                    res += 1
            else:
                if s[i-1] == '0' and count1 != 0:
                    count1 = 1
                else:
                    count1 += 1
                if count0 >= count1:
                    res += 1

        return res
