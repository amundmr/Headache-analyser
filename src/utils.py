from ics import Calendar, Event  # pip install ics
import arrow

def read_ics(filename):
    f = open(filename, "r")
    data = f.readlines()
    string = ""
    for line in data:
        string += line
    c = Calendar(string)
    e = list(c.timeline)
    return e

def get_max_strength_of(event):
    data = event.description

    strengths = []
    in_times = False
    for line in data.split("\n"):
        if "Times:" in line:
            in_times = True
            continue
        elif "Coffe:" in line:
            break
        
        if in_times == True:
            strengths.append(int(eval(line.split(":")[-1])*10))
    try: 
        maks = max(strengths)
    except:
        maks = None
    return maks
