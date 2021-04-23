# Headache analyser

This small software aims to make the analyzation of headaches eazy. It is based on having a separate calendar with only headache events, where you manually create a new event and fill in the details of the template when a headache occur. This calendar can then be exported from any calendar client and to a `.ics` file, which this program can work with.



Google calendar headache entry template: 
```
Start: 0900
Times: 
  1200: 3/10
  1500: 4/10
  2050: 7/10
Coffe: no
Wine: no 
Sleep offset: 0 
Sleep deprivation: 0
Maxalt: no 
Maxalt fixed it:
```


# Commands

## read_ics(filename)

Takes filename of .ics file containing only headache events, returns list of events using the ics package.


## get_averages(events)
Takes list of events, prints averages of how many times per timeperiod headaches occur.

Example output:
```
---Averages---
Average per
        Day:    0.22
        Week:   1.51
        Month:  6.43
        Year:   77.14
```


## get_logstats(events)
Takes list of events, prints statistics about the logging itself.

Example output:
```
---Logging statistics---
Total duration of logging: 7 months
From 2020-09-24, to 2021-04-20
First logging: 7 months ago, last logging: 3 days ago
```

## plot_weekday(events)
Takes list of events, outputs bar plot with number of occurences vs weekday.

Example:
()[./assets/weekday_plot.png]


## plot_by_strength(events)
Takes list of events, outputs bar plot with number of occurences vs max strength of headache.

Example:
()[./assets/strength_plot.png]