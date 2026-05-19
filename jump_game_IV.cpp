class Solution {
public:
    int minJumps(vector<int>& arr) {
        unordered_map<int,unordered_set<int>> pos;
        int n = arr.size();
        for (int i = 0; i < n; i++) {
            int v = arr[i];
            if (pos.find(v) == pos.end()) {
                pos[v] = unordered_set<int>();
            }
            pos[v].insert(i);
        }

        deque<int> q;
        q.push_back(0);
        int steps = 0;

        unordered_set<int> visited;
        visited.insert(0);

        while (!q.empty()) {
            int s = q.size();
            for (int i = 0; i < s; i++) {
                int p = q.front();
                if (p == n-1) return steps;
                q.pop_front();

                if (p-1 >= 0 && visited.find(p-1) == visited.end()) {
                    visited.insert(p-1);
                    q.push_back(p-1);
                }

                if (p+1 < n && visited.find(p+1) == visited.end()) {
                    visited.insert(p+1);
                    q.push_back(p+1);
                }

                if (pos.find(arr[p]) != pos.end()) {
                    for (int v : pos[arr[p]]) {
                        if (visited.find(v) != visited.end()) {
                            continue;
                        }
                        visited.insert(v);
                        q.push_back(v);
                    }
                    pos.erase(arr[p]);
                }
                
            }
            steps++;
        }

        return -1;
    }
};