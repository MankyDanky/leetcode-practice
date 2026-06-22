class Solution {
public:
    int maxNumberOfBalloons(string text) {
        unordered_map<char,int> counter;
        for (char c : text) {
            if (counter.find(c) != counter.end()) {
                counter[c] += 1;
            } else {
                counter[c] = 1;
            }
        }

        int res = 10000000;
        for (char c : "ban") {
            if (c == 0) continue;
            if (counter.find(c) == counter.end()) {
                cout<<c<<endl;
                return 0;
            }
            res = min(res, counter[c]);
        }
        for (char c : "lo") {
            if (c == 0) continue;
            if (counter.find(c) == counter.end()) return 0;
            res = min(res, counter[c]/2);
        }

        return res;
    }
};
