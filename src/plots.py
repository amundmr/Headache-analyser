
def plot_weekday(events):
    from utils import get_max_strength_of
    weekdays = [0,0,0,0,0,0,0]
    avg_strengths = [0,0,0,0,0,0,0]
    strengths= [[],[],[],[],[],[],[]]
    weekday_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for event in events:
        weekdays[event.begin.weekday()] += 1
        strengths[event.begin.weekday()].append(get_max_strength_of(event))

    for i,s in enumerate(strengths):
        s = list(filter(None, s))
        avg_strengths[i] = sum(s)/len(s)

    colors = []
    data_color = [x / 10 for x in avg_strengths]

    import matplotlib.pyplot as plt
    from matplotlib.cm import ScalarMappable

    fig, ax = plt.subplots(figsize=(10, 7))

    my_cmap = plt.cm.get_cmap('tab10')
    colors = my_cmap(data_color)
    rects = ax.bar([1, 2, 3, 4, 5, 6, 7], weekdays, color=colors, tick_label = weekday_names)


    sm = ScalarMappable(cmap=my_cmap, norm=plt.Normalize(0,10))
    sm.set_array([])

    cbar = plt.colorbar(sm)
    cbar.set_label('Average Strength', rotation=270,labelpad=25)

  
    plt.ylabel("Occurences")
    plt.title("Headache weekday distribution")
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
    
    plt.bar([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], strengths, tick_label=strength_strings)
    plt.ylabel("Total occurences")
    plt.xlabel("Headache Strength")
    plt.title("Occurences of Headache Strengths")
    plt.show()