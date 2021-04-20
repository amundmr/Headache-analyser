from ics import Calendar, Event
filename = "./data/20210420.ics"
f = open(filename, "r")
data = f.readlines()
string = ""
for line in data:
    string += line
c = Calendar(string)
#print(type(c.events))
events = c.events
print(events.event())
