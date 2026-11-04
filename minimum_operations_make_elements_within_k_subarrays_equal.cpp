class Solution {
public:
    long long minOperations(vector<int>& nums, int x, int k) {
        // Way to make a given index to index + x - 1 all the same has a fixed optimal way to make them even
        // We select the indices that are NOT in any interval, and use dp with state being [index][remaining_intervals] to get a O(15*n * q) = O(n * q) solution where q is the time complexity it takes to compute the cost of making a given interval the same size
        // Will pass if q is <= sqrt(n)
        // Minimum way involves making all elements the median (proved in previous problems and STAT 231)
        // Sliding window to compute each length x's cost? Two heaps to get median efficiently
        // AND sum of lower heap and larger heap
        // Cost is the size of lower heap * median - sum of lower heap + sum of higher heap - size of higher heap * median
        // Precompute cost of each window

        

        multiset<int> lower;
        multiset<int> higher;
        long long lowerSum = 0;
        long long higherSum = 0;

        auto balance = [&]() {
            while (lower.size() > 0 && higher.size() > 0 && *(--lower.end()) > *(higher.begin())) {
                int l = *(--lower.end());
                int h = *(higher.begin());

                lower.erase(lower.find(l));
                higher.erase(higher.find(h));

                lowerSum -= l;
                higherSum -= h;

                lowerSum += h;
                higherSum += l;

                lower.insert(h);
                higher.insert(l);
            }

            while (lower.size() > higher.size() + 1) {
                int l = *(--lower.end());
                lower.erase(lower.find(l));
                lowerSum -= l;
                higherSum += l;
                higher.insert(l);
            }

            while (higher.size() > lower.size() + 1) {
                int h = *(higher.begin());
                higher.erase(higher.find(h));
                higherSum -= h;
                lowerSum += h;
                lower.insert(h);
            }
        };

        auto getMedian = [&]() {
            if (lower.size() > higher.size()) {
                return *(--lower.end());
            } else {
                return *(higher.begin());
            }
        };

        auto getCost = [&]() {
            int median = getMedian();

            long long cost = ((long long)lower.size() * median - lowerSum) + ((long long)higherSum - higher.size()*median);
            return cost;
        };

        for (int i = 0; i < x; i++) {
            lower.insert(nums[i]);
            lowerSum += nums[i];
            balance();
        }

        int n = nums.size();
        vector<long long> costs(n - x + 1);
        

        costs[0] = getCost();

        for (int i = x; i < n; i++) {
            // Remove (i - x)th element
            if (lower.find(nums[i-x]) != lower.end()) {
                lower.erase(lower.find(nums[i-x]));
                lowerSum -= nums[i-x];
            } else {
                higher.erase(higher.find(nums[i-x]));
                higherSum -= nums[i-x];
            }

            lower.insert(nums[i]);
            lowerSum += nums[i];

            balance();

            costs[i-x + 1] = getCost();
        }

        vector<vector<long long>> dp(n + 1, vector<long long>(k + 1, LLONG_MAX / 2));
        for (int i = 0; i < n + 1; i++) {
            dp[i][0] = 0;
        }

        for (int rem = 1; rem <= k; rem++) {
            for (int i = n - x; i >= 0; i--) {
                dp[i][rem] = min(dp[i+1][rem], costs[i] + dp[i+x][rem-1]);
            }
        }

        return dp[0][k];
    }
};
