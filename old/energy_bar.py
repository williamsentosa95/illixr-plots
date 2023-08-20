# Import libraries
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager

BASE_SZ = 14
TEXT_COLOR = '#202020'

label_font_size = 10
hatches = ['', "/", "xx", ""]

colors = ["cadetblue", "burlywood", "lightgreen", "plum", "indianred"]

def config_style():
    mpl.rcParams.update({'font.size': 10})

def __config_base_style(base_size=BASE_SZ):
    """Customize plot aesthetics."""
    mpl.rcParams['font.family'] = 'sans-serif'
    # Use a sensible *free* font.
    mpl.rcParams['font.sans-serif'] = 'Clear Sans'
    mpl.rcParams['font.size'] = base_size

    mpl.rcParams['axes.spines.top'] = False
    mpl.rcParams['axes.spines.right'] = False

    mpl.rcParams['axes.grid'] = True
    mpl.rcParams['axes.grid.axis'] = 'both'
    mpl.rcParams['axes.grid.which'] = 'both'

    mpl.rcParams['axes.edgecolor'] = '#808080'
    mpl.rcParams['axes.linewidth'] = 1.5
    mpl.rcParams['axes.titlesize'] = base_size
    mpl.rcParams['axes.labelsize'] = base_size
    mpl.rcParams['axes.labelweight'] = 'bold'

    mpl.rcParams['xtick.labelsize'] = base_size
    mpl.rcParams['xtick.color'] = '#606060'
    mpl.rcParams['xtick.major.size'] = 10
    mpl.rcParams['xtick.major.width'] = 1.5
    mpl.rcParams['xtick.minor.size'] = 6
    mpl.rcParams['xtick.minor.width'] = 1.5
    mpl.rcParams['xtick.direction'] = 'out'
    mpl.rcParams['xtick.major.pad'] = 8
    mpl.rcParams['xtick.minor.pad'] = 8

    mpl.rcParams['ytick.labelsize'] = base_size
    mpl.rcParams['ytick.color'] = '#606060'
    mpl.rcParams['ytick.major.size'] = 10
    mpl.rcParams['ytick.major.width'] = 1.5
    mpl.rcParams['ytick.minor.size'] = 6
    mpl.rcParams['ytick.minor.width'] = 1.5
    mpl.rcParams['ytick.direction'] = 'out'
    mpl.rcParams['ytick.major.pad'] = 8
    mpl.rcParams['ytick.minor.pad'] = 8

    mpl.rcParams['legend.fontsize'] = base_size
    mpl.rcParams['legend.frameon'] = True

plt.rcdefaults()
# __config_base_style()
config_style()
matplotlib.rcParams['pdf.fonttype'] = 42

def is_float(element) -> bool:
    try:
        float(element)
        return True
    except ValueError:
        return False

fig, ax = plt.subplots()
data_path = "data/energy_data.txt"

fig.set_size_inches(2, 4)

x_labels = []
data = []
width = 0.2       # the width of the bars: can also be len(x) sequence

textfile = open(data_path, "r")
line_num = 1
components = []

for line in textfile:
    if (line_num == 1):
        headers = line.strip('\n').split('\t')
        x_labels = headers[1:]
    else:  
        entries = line.strip().split("\t")
        components.append(entries[0])
        data_point = [float(i) for i in entries[1:]]
        data.append(data_point)
    line_num += 1


assert(len(components) == len(data))

bottom_data = [0] * len(x_labels)

for i in range(0, len(components)):
       ax.bar(x_labels, data[i], width, label=components[i], bottom=bottom_data, color=colors[i], edgecolor="black")
       for j in range(0, len(data[i])):
              bottom_data[j] += data[i][j]


ax.set_ylabel('Energy (W)')
ax.legend()

plt.savefig('energy.pdf', bbox_inches='tight')

plt.show()