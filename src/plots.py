
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
    from utils import get_max_strength_of

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