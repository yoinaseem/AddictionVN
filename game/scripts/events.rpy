init python:
    class Calendar(object):
        def __init__(self, WeekDays, Months, MonthDays, TimeOfDay, GameHour, Minutes, Day, MonthDay, Month):
            self.WeekDays = WeekDays
            self.Months = Months
            self.MonthDays = MonthDays
            self.TimeOfDay = TimeOfDay
            self.GameHour  = GameHour
            self.Minutes = Minutes
            self.Day = Day 
            self.MonthDay = MonthDay
            self.Month = Month

        @property 
        def Output(self):
            return  self.WeekDays[self.Day] + " " + self.Months[self.Month] + " " + str(self.MonthDay+1) + " " + str(self.GameHour).zfill(2) + ":" + str(self.Minutes).zfill(2)

        def AdvanceTime(self, hours):
            self.GameHour += hours
            if self.GameHour >= 24:
                self.GameHour -= 24
                self.Day += 1
                self.MonthDay += 1
            if self.Day >= 7:
                self.Day = 0 
            if self.MonthDay > self.MonthDays[self.Month]:
                self.Month += 1
                self.MonthDay = 0
            if self.Month >=12:
                self.Month = 0