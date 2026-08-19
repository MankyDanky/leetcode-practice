class Solution {
public:
    int maxNumberOfFamilies(int n, vector<vector<int>>& reservedSeats) {
        int res = 2 * n;
        unordered_map<int,vector<bool>> m;
        for (vector<int> v : reservedSeats) {
            int row = v[0];
            int seat = v[1];
            if (seat == 1 || seat == 10) continue;
            if (!m.contains(row)) {
                m[row] = {false, false, false};
            }

            if (seat == 1 || seat == 10) continue;
            if (4 <= seat && seat <= 7) {
                m[row][1] = true;
            } 
            if (seat <= 5) {
                m[row][0] = true;
            } else {
                m[row][2] = true;
            }
        }

        for (pair<int,vector<bool>> p : m) {
            vector<bool> v = p.second;
            res -= 1;
            if (v[0] == true && v[1] == true && v[2] == true) res -= 1;
        }
        return res;
    }
};
