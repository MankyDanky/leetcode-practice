class Solution {
public:
    int missingMultiple(vector<int>& nums, int k) {
        unordered_set<int> seen;
        for (int num : nums) {
            seen.insert(num);
        }
        int x = k;
        while (true) {
            if (!seen.contains(x)) {
                return x;
            }
            x += k;
        }
        return 0;
    }
};
