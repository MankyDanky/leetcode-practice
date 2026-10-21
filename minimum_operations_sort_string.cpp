class Solution {
public:
    int minOperations(string s) {
        int MX = 0;
        int MN = INT_MAX;
        for (char c : s) {
            MX = max(MX, (int)c);
            MN = min(MN, (int)c);
        }
        int MX_C = 0;
        int MN_C = 0;

        for (char c : s) {
            if ((int) c == MX) MX_C++;
            if ((int) c == MN) MN_C++;
        }
        string copy = s;
        sort(copy.begin(), copy.end());
        if (copy == s) return 0;
        if (s.size() == 2 && s[0] > s[1]) return -1;
        if (s[0] == MX && s[s.size()-1] == MN && MX_C == 1 && MN_C == 1) return 3;
        if (s[0] == MN || s[s.size() - 1] == MX) return 1;
        return 2;
        
    }
};
