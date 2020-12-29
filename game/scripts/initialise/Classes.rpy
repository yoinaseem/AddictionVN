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

    class Place(object):
        def __init__(self, x, y, name, bg, unlocked):
            self.x = x
            self.y = y 
            self.name = name 
            self.bg = bg
            self.unlocked = unlocked

    class Player(object):
        def __init__(self, name, strength, charm, cash):
            self.name = name
            self.strength = strength 
            self.charm = charm 
            self.cash = cash 


    Places = []

    Places.append(Place(1000,500, "Bedroom", "bedroom", True))
    Places.append(Place(700,300, "Dorm", "dorm", True))
    Places.append(Place(200,500, "College", "college", True))
    Places.append(Place(500,100, "Street", "street", True))

    

