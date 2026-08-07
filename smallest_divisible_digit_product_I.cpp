class Solution {
public:
    int smallestNumber(int n, int t) {
        for (int num = n; true; num++) {
            int p = 1;
            int x = num;
            while (x != 0) {
                p *= x%10;
                x/=10;
            }
            if (p % t == 0) return num;
        }
        return 0;
    }
};
