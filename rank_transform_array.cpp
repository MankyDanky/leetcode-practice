class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        unordered_map<int,int> rank;

        set<int> nums;
        for (int num : arr) {
            nums.insert(num);
        }
        int r = 1;
        for (int num : nums) {
            rank[num] = r;
            r++;
        }

        for (int i = 0; i < arr.size(); i++) {
            arr[i] = rank[arr[i]];
        }
        return arr;
    }
};
