class Solution {
public:
    bool checkOverlap(int radius, int xCenter, int yCenter, int x1, int y1, int x2, int y2) {
        if (x1 <= xCenter && xCenter <= x2 && y1 <= yCenter && yCenter <= y2) {
            return true;
        }
        for (int i = x1; i <= x2; i++) {
            if ((i - xCenter) * (i - xCenter) + (y1 - yCenter) * (y1 - yCenter) <= radius * radius) return true;
            if ((i - xCenter) * (i - xCenter) + (y2 - yCenter) * (y2 - yCenter) <= radius * radius) return true;
        }
        for (int i = y1; i <= y2; i++) {
            if ((x1 - xCenter) * (x1 - xCenter) + (i - yCenter) * (i - yCenter) <= radius * radius) return true;
            if ((x2 - xCenter) * (x2 - xCenter) + (i - yCenter) * (i - yCenter) <= radius * radius) return true;
        }
        return false;
    }
};
