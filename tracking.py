from datetime import datetime
class tracking:
    def __init__(self):
        today = int(datetime.now().strftime("%d"))
        self.month = int(datetime.now().strftime("%m"))
        self.year = int(datetime.now().strftime("%Y"))
        self.day = today
        self.xAxe = []
        self.lasDaysCash = []
        self. lastDaysSells = []
        for i in range(5):
            self.xAxe.append(today - i)
            self.lasDaysCash.append(0)
            self.lastDaysSells.append(0)

        
    
        with open("assets/data/sells.txt", "r") as sellsFile:
            lines = sellsFile.readlines()
            for line in lines:
                date = line.split('-')[0]
                year = int(date.split('_')[0])
                month = int(date.split('_')[1])
                day = int(date.split('_')[2])
                if year == self.year or year >= self.year -1 and month == 1:
                    if month == self.month or month >= self.month -1 and day < 6:
                        if day >= self.day - 5:
                            for i in range(5):
                               if(day == self.day - i):
                                    self.lasDaysCash[i] += int(line.split('-')[1])
                                    self.lastDaysSells[i] += 1

    def sellsReport(self):
        return [self.xAxe, self.lastDaysSells]
    
    def sellsCash(self):
        return [self.xAxe, self.lasDaysCash]
trackingObject = tracking()
print(str(trackingObject.sellsReport()[1]))
print(str(trackingObject.sellsCash()[1]))
