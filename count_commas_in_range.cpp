class Solution {
public:
    int countCommas(int n) {
        int res = 0;
        for (int i = 1000; i <= n; i++) {
            int s = 0;
            int x = i;
            while (x != 0) {
                s += 1;
                x /= 10;
            }
            res += (s - 1) / 3;
        }
        return res;
    }
};
