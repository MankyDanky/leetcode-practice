class Solution {
public:
    long long minimumCost(int cost1, int cost2, int costBoth, int need1, int need2) {
        long long res = 0;
        if (costBoth < cost1 + cost2) {
            int b = min(need1, need2);
            need1 -= b;
            need2 -= b;
            res += (long long)b * costBoth;
            if (need1 > need2 && need1 > 0) {
                if (costBoth < cost1) {
                    res += (long long) costBoth*need1;
                    need1 = 0;
                }
            } else if (need2 > 0) {
                if (costBoth < cost2) {
                    res += (long long) costBoth * need2;
                    need2 = 0;
                }
            }
        }
        res += (long long) need2 * cost2;
        res += (long long) need1 * cost1;
        return res;
    }
};
