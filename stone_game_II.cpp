class Solution {
public:
    vector<vector<unordered_map<int,int>>> cache;

    int score(int pos, int m, bool alice, vector<int>& piles) {
        if (pos == piles.size()) return 0;
        if (cache[pos][alice].contains(m)) {
            return cache[pos][alice][m];
        }
        int res;
        if (alice) {
            res = -1000000000;
            int take = 0;

            for (int i = pos; i < piles.size() && i - pos + 1 <= 2*m; i++) {
                take += piles[i];
                int s = score(i+1, max(i - pos + 1, m), false, piles) + take;
                res = max(res, s);
            }
        } else {
            res = 1000000000;
            int take = 0;

            for (int i = pos; i < piles.size() && i - pos + 1 <= 2*m; i++) {
                take -= piles[i];
                int s = score(i+1, max(i - pos + 1, m), true, piles) + take;
                res = min(res, s);
            }
        }
        cache[pos][alice][m] = res;
        return res;
    }

    int stoneGameII(vector<int>& piles) {
        cache.resize(piles.size(), vector<unordered_map<int,int>>(2));
        int t = 0;
        for (int p : piles) {
            t += p;
        }
        int s = score(0, 1, true, piles);
        int b = (t - s)/2;
        int a = t - b;
        return a;
    }
};
