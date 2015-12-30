import time;

def main():
    numSundays = 0;
    SUNDAY = 0;
    day = 1;
    monthCodes = [6,2,2,5,0,3,5,1,4,6,2,4];
    leapYearCodes = [0,5,3,1,6,4,2];
    leapYearIndex = 0;
    isLeapYear = False;
    for year in xrange(1901,2001):
        lastDigits = year % 100;
        if ((year % 4 == 0) and not (year % 100 == 0)) or (year % 400 == 0):
            leapYearIndex = (leapYearIndex + 1) % 7;
            yearCode = leapYearCodes[leapYearIndex];
            isLeapYear = True;
        else:
            yearCode = (leapYearCodes[leapYearIndex] + (lastDigits % 4)) % 7;
            isLeapYear = False;
        if year < 2000:
            yearCode += 1;
        else:
            yearCode = 0;
        for month in range(0,len(monthCodes)):
            monthCode = monthCodes[month];
            if isLeapYear:
                if month == 0 or month == 1:
                    monthCode -= 1;
            if (monthCode + day + yearCode) % 7 == SUNDAY:
                numSundays += 1;
    print(numSundays);

start = time.time();
main();
print(time.time() - start);
