class Solution {
public:
    vector<string> res;
    int minRemoved = INT_MAX;
    set<string> added;

    void backtrack(string& s, int index, int curr, int removed, string& currS) {
        
        if (index == s.size()) {
            if (curr == 0 && removed <= minRemoved) {
                if (removed == minRemoved) {
                    if (!added.contains(currS)) {
                        res.push_back(currS);
                        added.insert(currS);
                    }
                } else {
                    res.clear();
                    added.clear();
                    added.insert(currS);
                    res.push_back(currS);
                    minRemoved = removed;
                }
            }
            return;
        }
        if (s[index] == ')') {
            if (curr > 0) {
                currS += ')';
                backtrack(s, index+1, curr - 1, removed, currS);
                currS.pop_back();
            }
            
            backtrack(s, index+1, curr, removed+1, currS);
        } else if (s[index] == '(') {
            currS += '(';
            backtrack(s, index+1, curr + 1, removed, currS);
            currS.pop_back();
            backtrack(s, index+1, curr, removed+1, currS);
        } else {
            currS += s[index];
            backtrack(s, index+1, curr, removed, currS);
            currS.pop_back();
        }
    }

    vector<string> removeInvalidParentheses(string s) {
        string p = "";
        backtrack(s, 0, 0, 0, p);
        cout<<minRemoved<<endl;
        if (minRemoved == s.size()) return {""};
        return res;
    }
};
