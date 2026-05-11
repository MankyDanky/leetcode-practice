class Solution {
    public:
        vector<int> separateDigits(vector<int>& nums) {
            vector<int> res;
            int n = nums.size();
            res.reserve(n*2);
    
            for (int i = 0; i < n; i++) {
                stack<int> digits;
                while (nums[i] != 0) {
                    digits.push(nums[i]%10);
                    nums[i]/=10;
                }
                while (!digits.empty()) {
                    res.push_back(digits.top());
                    digits.pop();
                }
            }
    
            return res;
        }
    };