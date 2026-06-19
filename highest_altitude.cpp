class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int h = 0;
        int res = 0;
        for (int g : gain) {
            h += g;
            res = max(res, h);
        }
        return res;
    }
};
