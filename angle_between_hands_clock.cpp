class Solution {
public:
    double angleClock(int hour, int minutes) {
        double hourHand = ((double)(hour % 12) + ((double)minutes / 60.0)) / 12;
        double minuteHand = (double)minutes/60.0;

        if (hourHand < minuteHand) {
            return 360.0 * min(minuteHand - hourHand, hourHand - minuteHand + 1);
        } else {
            return 360.0 * min(hourHand - minuteHand, minuteHand - hourHand + 1);
        }
    }
};
