class Solution {
public:
    vector<long long> cache;
    
    long long cost(int index, vector<int>& costs) {
        long long minCost = INT_MAX;
        if (cache[index] != -1) return cache[index];
        if (index == costs.size()) return 0;
        for (int i = 1; i <= 3; i++) {
            if (i+index > costs.size()) break;
            minCost = min(minCost, costs[index+i - 1] + i*i + cost(index+i, costs));
        }
        cache[index] = minCost;
        return minCost;
    }

    int climbStairs(int n, vector<int>& costs) {
        cache.resize(costs.size() + 1, -1);

        return cost(0, costs);
    }
};
