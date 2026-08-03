class Solution {
public:
    vector<vector<bool>> cached;
    vector<vector<int>> cache;

    int score(int pos, bool alice, vector<int>& stoneValue) {
        if (pos == stoneValue.size()) {
            return 0;
        }
        if (cached[pos][alice]) {
            return cache[pos][alice];
        }
        int res;
        if (alice) {
            res = -1000000000;
            int s = 0;
            for (int i = pos; i <= pos + 2 && i < stoneValue.size(); i++) {
                s += stoneValue[i];
                res = max(res, s + score(i+1, false, stoneValue));
            }
        } else {
            res = 1000000000;
            int s = 0;
            for (int i = pos; i <= pos + 2 && i < stoneValue.size(); i++) {
                s -= stoneValue[i];
                res = min(res, s + score(i+1, true, stoneValue));
            }
        }
        cache[pos][alice] = res;
        cached[pos][alice] = true;
        return res;

    }

    string stoneGameIII(vector<int>& stoneValue) {
        cached.resize(stoneValue.size(), vector<bool>(2, false));
        cache.resize(stoneValue.size(), vector<int>(2));

        int s = score(0, true, stoneValue);
        return (s > 0 ? "Alice" : (s < 0 ? "Bob" : "Tie"));
    }
};
