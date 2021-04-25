def print_averages(events):
    from ics import Calendar, Event
    n_headaches = len(events)

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

def print_logstats(events):
    from ics import Calendar, Event
    start_date = events[0].begin
    end_date = events[-1].begin
    month_diff = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
    print("\n\n---Logging statistics---")
    print("Total duration of logging: %.0f months" % month_diff)
    print("From {}, to {}".format(start_date.date(), end_date.date()))
    print("First logging: {}, last logging: {}".format(start_date.humanize(), end_date.humanize()))