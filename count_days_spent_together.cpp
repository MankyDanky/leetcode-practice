class Solution {
public:
    int countDaysTogether(string arriveAlice, string leaveAlice, string arriveBob, string leaveBob) {
        vector<int> daysPerMonth = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        vector<int> prefixDaysPerMonth(12, 0);
        for (int i = 1; i < 12; i++) {
            prefixDaysPerMonth[i] = prefixDaysPerMonth[i-1] + daysPerMonth[i-1];
        }

        int dayArriveA = prefixDaysPerMonth[stoi(arriveAlice.substr(0, 2)) - 1] + stoi(arriveAlice.substr(3, 2));
        int dayLeaveA = prefixDaysPerMonth[stoi(leaveAlice.substr(0, 2)) - 1] + stoi(leaveAlice.substr(3, 2));

        int dayArriveB = prefixDaysPerMonth[stoi(arriveBob.substr(0, 2)) - 1] + stoi(arriveBob.substr(3, 2));
        int dayLeaveB = prefixDaysPerMonth[stoi(leaveBob.substr(0, 2)) - 1] + stoi(leaveBob.substr(3, 2));
 
        if (dayLeaveA < dayArriveB || dayLeaveB < dayArriveA) return 0;
        return min(dayLeaveB, dayLeaveA) - max(dayArriveA, dayArriveB) + 1;
    }
};
