class Solution {
public:
    vector<vector<vector<int>>> cache;

    int score(int l, int r, vector<int>& piles, bool alice) {
        if (l > r) {
            return 0;
        }
        if (cache[l][r][alice] != -1) return cache[l][r][alice];
        int res = 0;
        if (alice) {
            res = max(piles[l] + score(l+1, r, piles, false), piles[r] + score(l, r-1, piles, false));
        } else {
            res = min(-piles[l] + score(l+1, r, piles, true), -piles[r] + score(l, r-1, piles, true));
        }
        cache[l][r][alice] = res;
        return res;
    }

    bool stoneGame(vector<int>& piles) {
        int n = piles.size();

        cache.resize(n, vector<vector<int>>(n, vector<int>(2, -1)));

        int s = score(0, piles.size()-1, piles, true);
        return s > 0;
    }
};
