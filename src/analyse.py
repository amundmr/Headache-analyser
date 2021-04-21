from ics import Calendar, Event
filename = "./data/20210420.ics"
f = open(filename, "r")
data = f.readlines()
string = ""
for line in data:
    string += line
c = Calendar(string)
#print(type(c.events))
set_of_events = c.events
i=0
for event in set_of_events:
    if i<2:
        print(event)
    i+=1

class Headache:
    def __init__(self, 
                    date,
                    start,
                    max_pain,
                    coffe = False,
                    wine = False,
                    sleep_offset = 0,
                    sleep_depr = 0,
                    maxalt = False,
                    maxalt_fix = None,
                    ):
        self.date = date
        self.start = start
        self.max_pain = max_pain
        self.coffe = coffe
        self.wine = wine
        self.sleep_offset = sleep_offset
        self.sleep_depr = sleep_depr
        self.maxalt = maxalt
        self.maxalt_fix = maxalt_fix
        print("initiated headache event object")