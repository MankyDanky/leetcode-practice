class Solution {
public:
    int maxProduct(int n) {
        int maxD = 0;
        int secondMaxD = 0;
        while (n != 0) {
            if (n%10 >= maxD) {
                secondMaxD = maxD;
                maxD = n%10;
            } else if (n%10 > secondMaxD) {
                secondMaxD = n%10;
            }
            n/=10;
        }
        return maxD*secondMaxD;
    }
};
