class Solution {
public:
    int maximumLength(vector<int>& nums) {
        unordered_map<int,int> freq;
        for (int num : nums) {
            if (freq.find(num) == freq.end()) {
                freq[num] = 0;
            }
            freq[num] += 1;
        }

        int res = 1;

        for (pair<int,int> p : freq) {
            int count = 0;
            int k = p.first;
            int v = p.second;
            if (v == 1) continue;
            if (k == 1) {
                count = v - (!(v&1));
                res = max(res, count);
                continue;
            }
            count = 1;
            long long exp = (long long)k * k;
            while (freq.find(exp) != freq.end()) {
                count += 2;
                if (freq[exp] == 1) {
                    break;
                }
                if (exp > 1000000000) break;
                exp = exp * exp;
            }
            res = max(res, count);

        }
        return res;
    }
};
