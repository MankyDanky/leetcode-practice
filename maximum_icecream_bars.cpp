class Solution {
public:
    int maxIceCream(vector<int>& costs, int coins) {
        int maxCost = 1;
        int minCost = 1000000;

        for (int c : costs) {
            maxCost = max(maxCost, c);
            minCost = min(minCost, c);
        }

        vector<int> counts(maxCost - minCost + 1);

        int n = costs.size();

        for (int c : costs) {
            counts[c - minCost] += 1;
        }

        vector<int> prefix(counts);

        for (int i = 1; i < maxCost - minCost + 1; i++) {
            prefix[i] += prefix[i-1];
        }

        vector<int> sortedCosts(n);

        for (int c : costs) {
            int index = --prefix[c - minCost];
            sortedCosts[index] = c;
        }

        for (int i = 0; i < n; i++) {
            cout<<sortedCosts[i]<<' ';
        }
        cout<<endl;

        int res = 0;
        while (res < n) {
            if (coins >= sortedCosts[res]) {
                coins -= sortedCosts[res];
                res += 1;
            } else {
                break;
            }
        }

        return res;
    }
};
