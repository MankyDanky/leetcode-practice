class Solution {
public:
    int reverseDegree(string s) {
        int n = s.size();
        int res = 0;
        for (int i = 0; i < n; i++) {
            res += (26 - s[i] + 'a') * (i+1);
        }
        return res;
    }
};
