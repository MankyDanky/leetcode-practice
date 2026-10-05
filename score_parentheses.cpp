class Solution {
public:
    int scoreOfParentheses(string s) {
        return score(s, 0, s.size() - 1);
    }

    int score(string& s, int start, int end) {

        if (start >= s.size() || start >= end) return 0;
        int curr = 1;
        int i;
        for (i = start + 1; curr != 0; i++) {
            if (s[i] == '(') {
                curr += 1;
            } else {
                curr -= 1;
            }
        }
        
        int part = i - 1;
        int first = 1;
        if (part > start + 1) first = 2 * score(s, start + 1, part - 1);

        return first + score(s, part + 1, end);
    }
};
