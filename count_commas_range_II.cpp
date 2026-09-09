class Solution {
public:
    long long countCommas(long long n) {
        long long res = 0;
        int digits = 0;
        long long copy = n;
        while (copy != 0) {
            digits += 1;
            copy /= 10;
        }

        int commas = (digits - 1) / 3;

        long long ref = 1;
        int offset = (digits - 1 + 3) % 3;
        int targetD = digits - offset;
        for (int i = 1; i < targetD; i++) {
            ref *= 10LL;
        }
        res += (long long)(n - ref + 1) * commas;

        while (commas > 0) {
            commas -= 1;
            ref /= 1000;
            res += commas * ref * 999;
        }
        return res;
    }
};
