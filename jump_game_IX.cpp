class Solution {
    public:
        vector<int> maxValue(vector<int>& nums) {
            int n = nums.size();
            int r = n-1;
    
            multiset<int> reachable;
            set<int> indices;
    
            vector<pair<int,int>> s;
            s.reserve(n);
    
            for (int i = 0; i < n; i++) {
                s.push_back({nums[i], i});
            }
    
            sort(s.begin(), s.end());
            reverse(s.begin(), s.end());
    
            vector<int> res(n);
    
            for (int i = 0; i < n; i++) {
    
                if (reachable.size() > 0) {
                    res[s[i].second] = *(--reachable.end());
                } else {
                    res[s[i].second] = s[i].first;
                }
    
                reachable.insert(res[s[i].second]);
                indices.insert(s[i].second);
    
                while (indices.size() > 0 && *(--(indices.end())) == r) {
                    
                    indices.erase(r);
                    reachable.erase(reachable.find(res[r]));
                    r -= 1;
                }
            }
    
            return res;
    
        }
    };