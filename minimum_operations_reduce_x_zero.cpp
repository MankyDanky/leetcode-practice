class Solution {
public:
    int minOperations(vector<int>& nums, int x) {
        unordered_map<int,int> positionsEnd;
        positionsEnd[0] = nums.size();
        int s = 0;
        int res = INT_MAX;
        for (int i = nums.size() - 1; i >= 0; i--) {
            s += nums[i];
            positionsEnd[s] = i;
            if (s == x) res = nums.size() - i;
        }
        s = 0;
        
        for (int i = 0; i < nums.size(); i++) {
            s += nums[i];

            if (positionsEnd.find(x - s) != positionsEnd.end()) {
                if (positionsEnd[x-s] <= i) continue;
                res = min(res, i + 1 + ((int)nums.size() - positionsEnd[x - s]));
            }
        }
        return res != INT_MAX ? res : -1;
    }
};
