class Solution {
public:
    int maxDepth(string s) {
        int res = 0;
        int curr = 0;
        for (char c : s) {
            if (c == '(') {
                curr += 1;
            } else if (c == ')') {
                curr -= 1;
            }
            res = max(res, curr);
        }
        return res;
    }
};
