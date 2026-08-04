class Solution {
public:
    vector<int> findMissingElements(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<int> res;
        int curr = nums[0] + 1;

        for (int i = 1; i < nums.size(); i++) {

            while (curr != nums[i]) {
                res.push_back(curr);
                curr++;
            }
            curr ++;
        }
        return res;
    }
};
