class Solution {
public:
    int minOperations(vector<int>& nums) {
        int n = nums.size();

        int zeroPos = -1;
        for (int i = 0; i < n; i++) {
            if (nums[i] == 0) {
                zeroPos = i;
                break;
            }
        }

        bool forward = true;
        bool backward = false;

        for (int i = zeroPos; i < zeroPos + n; i++) {
            if (nums[i % n] != i - zeroPos) {
                forward = false;
                break;
            }
        }

        if (!forward) {
            backward = true;
            for (int i = zeroPos; i > zeroPos - n; i--) {
                if (nums[(i + n) % n] != zeroPos - i) {
                    backward = false;
                    break;
                }
            }
        }

        if (!backward && !forward) return -1;

        if (backward) {
            return min(n - 1 - zeroPos, zeroPos + 1) + 1;
        } else {
            return min(zeroPos, 2 + n - zeroPos);
        }
    }
};
