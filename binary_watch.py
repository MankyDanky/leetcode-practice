class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        hours = {0 : ["0"], 1 : ["8", "4", "2", "1"], 2 : ["3", "5", "6", "9", "10"], 3 : ["7", "11"]}
        minutes = {0: ["00"], 1 : ["01", "02", "04", "08", "16", "32"], 2 : ["03", "05", "06", "09", "10", "12", "17", "18", "20", "24", "33", "34", "36", "40", "48"], 3 : ["07", "11", "13", "14", "19", "21", "22", "25", "26", "28", "35", "37", "38", "41", "42", "44", "49", "50", "52", "56"], 4 : ["15", "23", "27", "29", "30", "39", "43", "45", "46", "51", "53", "54", "57", "58"], 5 : ["31", "47", "55", "59"]}
        output = []
        for i in range(min(4, turnedOn+1)):
            if turnedOn-i > 5:
                continue
            for hour in hours[i]:
                for minute in minutes[turnedOn-i]:
                    output.append(hour + ":" + minute)
        return output