class Solution {
public:
    string mapWordWeights(vector<string>& words, vector<int>& weights) {
        string res = "";

        for (string& word : words) {
            int weight = 0;
            for (char c : word) {
                weight += weights[c - 'a'];
            }
            res += 'z' - (weight % 26);
        }
        return res;
    }
};
