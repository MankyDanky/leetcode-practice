class Solution {
public:
    bool checkString(string s) {
        bool b = false;
        for (char c : s) {
            if (c == 'b') {
                b = true;
            } else {
                if (b == true) return false;
            }
        }
        return true;
    }
};
