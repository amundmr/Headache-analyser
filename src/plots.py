
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
    print(avg_strengths)
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    
    cmap = mpl.cm.hsv
    norm = mpl.colors.Normalize(vmin=0, vmax=10)
    colors = []
    for i in avg_strengths:
        colors.append(cmap(norm(i)))

    plt.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap),
              orientation='vertical', label='Headache strength')
    plt.bar(weekday_names,weekdays, color = colors)
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