from ics import Calendar, Event  # pip install ics
from utils import *
from prints import *
from plots import *

filename = "./data/20210420.ics"
event_lst = read_ics(filename)


print_averages(event_lst)
print_logstats(event_lst)

plot_weekday(event_lst)
plot_by_strength(event_lst)


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