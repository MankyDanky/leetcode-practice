class Solution {
public:
    bool canAliceWin(int n) {
        int d = 10;
        bool alice = false;
        while (n - d >= 0) {
            n -= d;
            d -= 1;
            alice = !alice;
        }
        return alice;
    }
};
