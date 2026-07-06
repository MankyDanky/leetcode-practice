class Solution {
public:
    int removeCoveredIntervals(vector<vector<int>>& intervals) {
        

        
        priority_queue<pair<int,int>> q;

        sort(intervals.begin(), intervals.end(), [&](const vector<int>& a, const vector<int>& b) {
            return a[1] < b[1] || (a[1] == b[1] && a[0] > b[0]);
        });

        int n = intervals.size(); 

        for (int i = 0; i < n; i++) {
            vector<int> v = intervals[i];
            while (!q.empty() && q.top().first >= v[0]) {
                q.pop();
            }
            q.push({v[0], i});
        }
        return q.size();
    }
};
