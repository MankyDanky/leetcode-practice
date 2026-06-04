class Solution {
public:
    int totalWaviness(int num1, int num2) {
        int res = 0;

        for (int num = num1; num <= num2; num++) {
            vector<int> digits;
            int x = num;
            while (x != 0) {
                digits.push_back(x % 10);
                x /= 10;
            }
            for (int i = 1; i < digits.size() - 1; i++) {
                if ((digits[i] < digits[i+1] && digits[i] < digits[i-1]) || (digits[i] > digits[i+1] && digits[i] > digits[i-1])) {
                    res += 1;
                }
            }
        }
        return res;
    }
};
