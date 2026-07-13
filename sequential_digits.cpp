class Solution {
public:
    vector<int> sequentialDigits(int low, int high) {
        vector<int> res;
        for (int k = 1; k < 10; k++) {
            for (int s = 1; s+k <= 10; s++) {
                int num = 0;
                for (int d = s; d < s+k; d++) {
                    num *= 10;
                    num += d;
                }
                if (low <= num && num <= high) {
                    res.push_back(num);
                }
            }
        }   
        return res;
    }
};
