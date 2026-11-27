class Solution {
public:
    int maximumSaleItems(vector<vector<int>>& items, int budget) {
        int n = items.size();
        vector<int> counts(n, 1);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                if (items[j][0] % items[i][0] == 0) counts[i]++;
            }
        }

        vector<vector<int>> dp(n+1, vector<int>(budget+1, 0));

        for (int i = n-1; i >=0; i--) {
            for (int b = budget; b >= 0; b--) {
                dp[i][b] = dp[i+1][b];
                if (items[i][1] <= b) {
                    dp[i][b] = max(dp[i][b], dp[i+1][b-items[i][1]] + counts[i]);
                }
            }
        }

        int c = 0;
        for (int i = 0; i < n; i++) {
            if (items[i][1] < items[c][1]) {
                c = i;
            }
        }

        int res = 0;
        for (int b = budget; b >= 0; b--) {
            res = max(
                res,
                dp[0][b] + (budget - b) / items[c][1]
                );
        }
        return res;
    }
};
