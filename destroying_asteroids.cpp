class Solution {
    public:
        bool asteroidsDestroyed(int mass, vector<int>& asteroids) {
            sort(asteroids.begin(), asteroids.end());
            long long m = mass;
            for (int s : asteroids) {
                if (s > m) {
                    return false;
                }
                m += s;
            }
            return true;
        }
    };