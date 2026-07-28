class Solution {
public:
    string smallestPalindrome(string s) {
        vector<int> freq(26, 0);

        for (char c : s) {
            freq[c - 'a']++;
        }
        string res = "";

        char m = '#';

        for (int i = 0; i < 26; i++) {
            while (freq[i] > 1) {
                freq[i] -= 2;
                res += ('a' + i);
            }
            if (freq[i] == 1) {
                m = ('a' + i);
            }
        }

        string c;
        for (int i = res.size()-1; i >= 0; i--) {
            c += res[i];
        }
        if (m != '#')
            res += m;
        res += c;

        return res;
    }
};
