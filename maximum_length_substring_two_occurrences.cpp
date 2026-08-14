class Solution {
public:
    int maximumLengthSubstring(string s) {
        vector<int> counts(26, 0);
        int res = 1;
        int r = 0;
        int l = 0;
        for (char c : s) {
            
            counts[c - 'a']++;
            while (counts[c-'a'] > 2) {
                counts[s[l]-'a']--;
                l++;
            }
            res = max(res, r - l + 1);
            r += 1;
        }
        return res;
    }
};
