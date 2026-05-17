class Solution {
    public:
        bool canMake(vector<vector<int>>& tasks, int k) {
            for (vector<int>& task : tasks) {
                if (k < task[1]) {
                    return false;
                }
                k -= task[0];
            }
            return true;
        }
    
        int minimumEffort(vector<vector<int>>& tasks) {
            sort(tasks.begin(), tasks.end(), [](const vector<int>& a, const vector<int>& b) {
                return a[1] - a[0] > b[1] - b[0];
            });
    
            for (vector<int>& task : tasks) {
                cout<<task[0]<<' '<<task[1]<<endl;
            }
            int n = tasks.size();
            int l = 0;
            int r = 0;
            for (int i = 0; i < n; i++) {
                r += tasks[i][1];
                l += tasks[i][0];
            }
    
            while (l < r) {
                int m = (l + r) / 2;
    
                if (canMake(tasks, m)) {
                    r = m;
                } else {
                    l = m + 1;
                }
            }
    
            return l;
        }
    };