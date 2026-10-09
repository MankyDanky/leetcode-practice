class Solution {
public:
    int minInsertions(string s) {
        int score = 0;
        int res = 0;
        for (char c : s) {
            if (c == '(') {
                if (score % 2) {
                    res += 1;
                    score -= 1;
                }
                score += 2;
            } else {
                score -= 1;
                if (score < 0) {
                    res += 1;
                    score += 2;
                }
            }
        }
        res += score;
        return res;
    }
};
