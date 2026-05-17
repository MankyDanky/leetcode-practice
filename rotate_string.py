class Solution {
public:
    bool rotateString(string s, string goal) {
        string search = goal+goal;

        if (s.size() == goal.size() && search.find(s) != string::npos) {
            return true;
        }
        return false;
    }
};