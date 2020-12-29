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
        def DateTime(self):
            Output = self.WeekDays[self.Day] + " " + self.Months[self.Month] + " " + str(self.MonthDay+1) + " " + str(self.GameHour).zfill(2) + ":" + str(self.Minutes).zfill(2)
            return Output

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
        def __init__(self, x, y, name, cfname, isActive):
            self.x = x
            self.y = y 
            self.name = name 
            self.cfname = cfname
            self.isActive = isActive

        @property
        def BG_Image(self):
            FilePath = "images/places/backgrounds/" + self.cfname + ".jpg"
            if renpy.loadable(FilePath):
                return FilePath
            else:
                return "images/places/backgrounds/dorm.jpg"

        def Unlock(self):
            self.isActive = True

        def Lock(self):
            self.isActive = False

        @property
        def MapIcon(self):
            global Chapter
            global Sequence
            DefOutput = "images/places/icons/none.png"
            Output = "/image/places/icons/" + self.cfname + ".png"
            AltOutput = "/image/places/icons/" + self.cfname + str(Chapter) + "_" + str(Sequence) + ".png"
            if renpy.loadable(AltOutput):
                return AltOutput
            if renpy.loadable(Output):
                return Output
            return DefOutput



    Places = []
    Places.append(Place(1000,500, "Bedroom", "bedroom", True))
    Places.append(Place(700,300, "Dorm", "dorm", True))
    Places.append(Place(200,500, "College", "college", True))
    Places.append(Place(500,100, "Street", "street", True))



    class People(object):
        def __init__(self, firstname, lastname, cfname, location, isActive):
            self.fname = firstname
            self.lname = lastname
            self.cfname = cfname
            self.location = location
            self.isActive = isActive

        @property
        def FullName(self):
            Output = self.fname + " " + self.lname
            return Output

        def Unlock(self):
            self.isActive = True

        def Lock(self):
            self.isActive = False

        @property
        def Avatar(self):
            global Location
            Output = "images/avatars/" + self.cfname + "_" + CFLocationName() +".png"

    Characters = []
    Characters.append(People("Test", "Girl", "test", "Dorm", True))

    class ClickObject(object):
        def __init__(self, name, cfname, location, clickType, isActive, tip):
            self.name = name
            self.cfname = cfname 
            self.location = location
            self.clickType = clickType 
            self.isActive = isActive
            self.tip = tip
        
        @property
        def Image(self):
            Output = "images/clickObjects/" + "_" + self.location + ".png"
            return Output

    ClickObjects = []

    ClickObjects.append(ClickObject("Test Object", "test_obj_01", "Bedroom", "Object", True, "Test Object"))



    class Player(object):
        def __init__(self, name, intelligence, tolerance, cash):
            self.name = name
            self.intelligence = intelligence 
            self.tolerance = tolerance 
            self.cash = cash 



    def CFLocationName():
        global Location
        global Places 
        for q in Places:
            if Location == q.name:
                return q.bgname
        return ""

    def CFLocationNum():
        global Location
        global Places 
        for q, i in enumerate(Places):
            if Location == q.name:
                return i
        return -1

