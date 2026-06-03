class Solution {
public:
    int earliestFinishTime(vector<int>& landStartTime, vector<int>& landDuration, vector<int>& waterStartTime, vector<int>& waterDuration) {
        vector<pair<int,int>> landTimes;
        vector<pair<int,int>> waterTimes;

        int m = landStartTime.size();
        int n = waterStartTime.size();

        for (int i = 0; i < m; i++) {
            landTimes.push_back({landDuration[i] + landStartTime[i], landStartTime[i]});
        }

        for (int i = 0; i < n; i++) {
            waterTimes.push_back({waterDuration[i] + waterStartTime[i], waterStartTime[i]});
        }

        

        sort(landTimes.begin(), landTimes.end());
        sort(waterTimes.begin(), waterTimes.end());

        cout<<waterTimes[0].first<<endl;

        int t1 = 1000000000;
        int t2 = 1000000000;

        for (int i = 0; i < m; i++) {
            if (landTimes[i].second <= waterTimes[0].first) {
                t2 = min(t2, landTimes[i].first - landTimes[i].second + waterTimes[0].first);
            } else {
                t2 = min(t2, landTimes[i].first);
                break;
            }
        }

        for (int i = 0; i < n; i++) {
            if (waterTimes[i].second <= landTimes[0].first) {
                t2 = min(t2, waterTimes[i].first - waterTimes[i].second + landTimes[0].first);
            } else {
                t2 = min(t2, waterTimes[i].first);
                break;
            }
        }

        return min(t1, t2);
    }
};
