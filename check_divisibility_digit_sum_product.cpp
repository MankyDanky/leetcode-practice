class Solution {
public:
    bool checkDivisibility(int n) {
        int prod = 1;
        int sum = 0;
        int x = n;
        while (x != 0) {
            int d = x % 10;
            prod *= d;
            sum += d;
            x/=10;
        }
        return n % (sum + prod) == 0;
    }
};
