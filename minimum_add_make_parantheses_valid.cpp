class Solution {
public:
    int minAddToMakeValid(string s) {
     int curr = 0;
     int res = 0;
     for (char c : s) {
        if (c == '(') {
            curr += 1;
        } else {
            curr -= 1;
            if (curr < 0) {
                curr += 1;
                res += 1;
            }
        }
     }
     res += curr;
     return res;   
    }
};
