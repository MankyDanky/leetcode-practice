class Solution {
public:
    int n;
    vector<int> parents;
    string chars;
    vector<optional<vector<int>>> cache;
    vector<int> next(int node) {
        if (node == 0) {
            vector<int> res(26, -1);
            res[chars[node] - 'a'] = 0;
            return res;
        }
        if (cache[node].has_value()) return cache[node].value();

        vector<int> sub = next(parents[node]);
        sub[chars[node] - 'a'] = node;
        cache[node] = sub;
        return sub;

    }
    vector<int> cache2;

    int size(vector<vector<int>>& children, int node) {
        if (children[node].size() == 0) return 1;
        if (cache2[node] != -1) return cache2[node];
        int res = 1;
        for (int c : children[node]) {
            res += size(children, c);
        }
        cache2[node] = res;
        return res;
    }
    


    vector<int> findSubtreeSizes(vector<int>& parent, string s) {
        n = parent.size();
        parents = parent;
        chars = s;
        cache.resize(n, nullopt);
        cache2.resize(n, -1);

        vector<int> newParents(n, -1);
        vector<vector<int>> children(n);

        for (int i = 1; i < n; i++) {
            vector<int> p = next(parents[i]);
            if (p[chars[i] - 'a'] != -1) {
                newParents[i] = p[chars[i] - 'a'];
                children[p[chars[i] - 'a']].push_back(i);
            } else {
                newParents[i] = parent[i];
                children[parent[i]].push_back(i);
            }
        }
        vector<int> res(n, 0);

        for (int i = 0; i < n; i++) {
            res[i] = size(children, i);
        }
        return res;

    }
};
