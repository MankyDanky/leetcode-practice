class Solution {
public:
    int rotatedDigits(int n) {
        int res = 0;
        for (int num = 1; num <= n; num++) {
            bool has = false;
            bool valid = true;
            int c = num;
            while (c != 0) {
                int d = c % 10;
                c /= 10;
                if (d == 2 || d == 5 || d == 6 || d == 9) {
                    has = true;
                } else if (d == 3 || d == 4 || d == 7) {
                    valid = false;
                }
            }

            if (valid && has) {
                res += 1;
            }
        }

        return res;
    }
};