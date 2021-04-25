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
    from fractions import Fraction
    import re
    data = event.description

    strengths = []
    in_times = False
    
    data_lst = re.split('\n|<br>',data)

    for line in data_lst:
        if "Times:" in line:
            in_times = True
            continue
        elif "Coffe:" in line:
            break
        
        if in_times == True:
            try:
                s = int(float(Fraction(line.split(":")[-1]))*10)
                strengths.append(s)
            except:
                continue

        continue
    try: 
        maks = max(strengths)
    except:
        maks = None

    return maks
