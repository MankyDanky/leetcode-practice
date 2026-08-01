class Solution {
public:
    bool canWin(int l, int r, vector<int>& nums, int score, int otherScore, bool p1) {
        if (l > r) {
            return p1 ? score >= otherScore : score > otherScore;
        }
        if (!canWin(l+1, r, nums, otherScore, score + nums[l], !p1)) {
            return true;
        }
        if (!canWin(l, r-1, nums, otherScore, score + nums[r], !p1)) {
            return true;
        }
        return false;
    }

    bool predictTheWinner(vector<int>& nums) {
        return canWin(0, nums.size()-1, nums, 0, 0, true);
    }
};
