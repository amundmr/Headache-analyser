from ics import Calendar, Event  # pip install ics
from utils import *
from prints import *
from plots import *

filename = "./data/20210420.ics"
event_lst = read_ics(filename)


#print_averages(event_lst)
#print_logstats(event_lst)

plot_weekday(event_lst)
#plot_by_strength(event_lst)