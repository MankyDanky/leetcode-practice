class Solution {
public:
    vector<string> b;
    int n;
    vector<vector<pair<long long, long long>>> cache;
    const long long MOD = 1000000007;

    pair<long long,long long> dp(int i, int j) {
        if (i < 0 || j < 0) return {0,0};

        if (i == 0 && j == 0) return {0,1};

        if (b[i][j] == 'X') return {0,0};

        if (cache[i][j].first != -1) return cache[i][j];

        pair<long long,long long> up = dp(i-1, j);
        pair<long long,long long> left = dp(i,j-1);
        pair<long long,long long> upleft = dp(i-1,j-1);

        long long maxValue = max(up.first, max(left.first, upleft.first));
        long long count = 0;

        if (up.first == maxValue) {
            count += up.second;
        }
        if (left.first == maxValue) {
            count += left.second;
        }
        if (upleft.first == maxValue) {
            count += upleft.second;
        }
        if (count == 0) {
            cache[i][j] = {0,0};
            return cache[i][j];
        }
        if (i != n-1 || j != n-1) maxValue += b[i][j] - '0';

        cache[i][j] = {maxValue % MOD, count % MOD};
        return cache[i][j];
    }

    vector<int> pathsWithMaxScore(vector<string>& board) {
        b = board;
        n = b.size();
        cache.resize(n, vector<pair<long long, long long>>(n, {-1, -1}));

        pair<long long, long long> res = dp(n-1,n-1);

        return {(int)res.first, (int)res.second};
    }
};
