class Solution {
public:
    string processStr(string s) {
        vector<char> res;
        for (char c : s) {
            if (c == '*') {
                if (res.size() > 0) {
                    res.pop_back();
                }
            } else if (c == '%') {
                reverse(res.begin(), res.end());
            } else if (c == '#') {
                vector<char> co(res);
                res.insert(res.end(), co.begin(), co.end());
            } else {
                res.push_back(c);
            }
        }

        string r = "";

        for (char c : res) {
            r += c;
        }
        return r;
    }
};
