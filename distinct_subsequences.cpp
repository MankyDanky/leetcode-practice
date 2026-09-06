class Solution {
public:
    vector<vector<int>> cache;
    int dp(int i, int j, string& s, string & t) {
        if (i == s.size()) return j == t.size();
        if (j == t.size()) return 1;
        if (cache[i][j] != -1) return cache[i][j];
        int res = 0;
        if (s[i] == t[j]) res += dp(i+1, j+1, s, t);
        res += dp(i+1, j, s, t);
        return cache[i][j]=res;
    }

    int numDistinct(string s, string t) {
        cache.resize(s.size(), vector<int>(t.size(), -1));
        if (s.size() < t.size()) return 0;
        return dp(0,0,s,t);
    }
};
