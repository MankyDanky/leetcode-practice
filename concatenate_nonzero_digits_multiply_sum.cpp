class Solution {
public:
    long long sumAndMultiply(int n) {
        if (n == 0) return 0;

        int sum = 0;
        vector<int> digits;

        while (n != 0) {
            int d = n % 10;
            sum += d;
            if (d != 0) {
                digits.push_back(d);
            }

            n/=10;
        }

        reverse(digits.begin(), digits.end());

        int x = 0;
        
        for (int d : digits) {
            x *= 10;
            x += d;
        }

        return (long long) sum * x;
    }
};
