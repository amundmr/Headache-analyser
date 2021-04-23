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

def get_averages(events):
    n_headaches = len(events)

    print(n_headaches)
    start_date = events[0].begin
    end_date = events[-1].begin

    diff = end_date-start_date

    month_diff = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
    
    avg_per_day = n_headaches/diff.days
    avg_per_week = n_headaches/(diff.days/7)
    avg_per_month = n_headaches/month_diff
    avg_per_year = n_headaches/(month_diff/12)

    print("\n\n---Averages---")
    print("Average per")
    print("\tDay: \t%.2f" % avg_per_day)
    print("\tWeek: \t%.2f" % avg_per_week)
    print("\tMonth: \t%.2f" % avg_per_month)
    print("\tYear: \t%.2f" % avg_per_year)
    
    return avg_per_day, avg_per_week, avg_per_month, avg_per_year

def get_logstats(events):
    start_date = events[0].begin
    end_date = events[-1].begin
    month_diff = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
    print("\n\n---Logging statistics---")
    print("Total duration of logging: %.0f months" % month_diff)
    print("From {}, to {}".format(start_date.date(), end_date.date()))
    print("First logging: {}, last logging: {}".format(start_date.humanize(), end_date.humanize()))


def plot_weekday(events):
    weekdays = [0,0,0,0,0,0,0]
    weekday_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for event in events:
        weekdays[event.begin.weekday()] += 1
    
    import matplotlib.pyplot as plt
    #TODO: Add colors to bars dependent on average headache strength
    plt.bar(weekday_names,weekdays)
    plt.ylabel("Total occurences")
    plt.show()

def plot_by_strength(events):
    import matplotlib.pyplot as plt
    strengths = [0,0,0,0,0,0,0,0,0,0] # Elem 1 is # occurences of 1/10 strength, Elem 10 is # occurences of 10/10 strength
    strength_strings = [r"$\frac{1}{10}$", r"$\frac{2}{10}$", r"$\frac{3}{10}$", r"$\frac{4}{10}$", r"$\frac{5}{10}$", r"$\frac{6}{10}$", r"$\frac{7}{10}$", r"$\frac{8}{10}$", r"$\frac{9}{10}$", r"$\frac{10}{10}$", ]

    for event in events:
        try:
            max_strength = get_max_strength_of(event)
            strengths[max_strength] += 1
        except:
            continue
    
    plt.bar(strength_strings, strengths)
    plt.ylabel("Total occurences")
    plt.show()
    
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
