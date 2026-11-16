class Solution {
public:
    string digitSum(string s, int k) {
        
        while (s.size() > k) {
            string nextS = "";
            for (int i = 0; i < s.size(); i += k) {
                int sum = 0;
                for (int j = i; j < i + k && j < s.size(); j++) {
                    sum += s[j] - '0';
                }
                nextS += to_string(sum);
            }
            s = nextS;
        }
        return s;
        
    }
};
