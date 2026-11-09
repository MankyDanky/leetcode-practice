class Solution {
public:
    vector<int> busiestServers(int k, vector<int>& arrival, vector<int>& load) {
        set<int> available;
        for (int i = 0; i < k; i++) {
            available.insert(i);
        }

        vector<int> loaded(k, 0);

        priority_queue<pair<int,int>> q;
        int ind = -1;
        for (int time : arrival) {
            ind += 1;
            while (!q.empty() && -1*(q.top().first) <= time) {
                pair<int,int> p = q.top();
                q.pop();
                available.insert(p.second);
            }
            if (available.size() == 0) continue;

            auto it = available.lower_bound(ind % k);
            if (it == available.end()) {
                it = available.lower_bound(0);
            }
            int comp = *it;

            loaded[comp] += 1;
            available.erase(comp);
            q.push({-1*(time + load[ind]), comp});
        }

        vector<int> res;
        int maxLoad = 0;
        for (int i = 0; i < k; i++) {
            if (loaded[i] == maxLoad) {
                res.push_back(i);
            } else if (loaded[i] > maxLoad) {
                maxLoad = loaded[i];
                res.clear();
                res.push_back(i);
            }
        }
        return res;
    }
};
