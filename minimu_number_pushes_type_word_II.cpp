class Solution {
public:
    int minimumPushes(string word) {
        vector<int> freq(26, 0);
        for (char c : word) {
            freq[c - 'a']++;
        }

        sort(freq.begin(), freq.end());
        reverse(freq.begin(), freq.end());

        int res = 0;
        vector<int> counts(4, 0);
        int p = 0;
        for (int f : freq) {
            res += f*(p+1);
            counts[p] += 1;
            if (counts[p] == 8) {
                p += 1;
            }
        }
        return res;
    }
};
