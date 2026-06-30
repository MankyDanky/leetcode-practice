class Solution {
public:
    int numberOfSubstrings(string s) {
        long long nt = 0;
        int l = 0;
        int n = s.size();
        vector<int> counts(3,0);
        for (int r = 0; r < n; r++) {
            counts[s[r] - 'a']++;
            while (min(min(counts[0], counts[1]), counts[2]) > 0) {
                counts[s[l] - 'a']--;
                l += 1;
            }
            nt += (r - l + 1);
        }

        long long t = ((long long) n * (n+1))/2;

        return t - nt;
    }
};
