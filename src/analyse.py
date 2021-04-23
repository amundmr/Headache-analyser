from ics import Calendar, Event  # pip install ics
import utils

filename = "./data/20210420.ics"
event_lst = utils.read_ics(filename)


#utils.get_averages(event_lst)
#utils.get_logstats(event_lst)

#utils.plot_weekday(event_lst)
#utils.plot_by_strength(event_lst)
utils.get_max_strength_of(event_lst[-1])

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