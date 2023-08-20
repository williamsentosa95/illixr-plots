# Import libraries
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager

BASE_SZ = 18
TEXT_COLOR = '#202020'

label_font_size = 12

def config_style():
    mpl.rcParams.update({'font.size': 15})

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
data_path = "data/latency_ape.txt"

fig.set_size_inches(6, 3.5)

line_num = 1

rtts = []
easy = []
medium = []
hard = []

textfile = open(data_path, "r")

for line in textfile:
    if (line_num == 1): # process the header
        headers = line.strip('\n').split('\t')
    else:
        entries = [float(i) for i in line.strip('\n').split('\t')]  
        rtts.append(int(entries[0]))
        easy.append(entries[1])
        medium.append(entries[2])
        hard.append(entries[3])
    line_num += 1
            
# Creating plot
ax.set_xticks(range(len(rtts)))
ax.set_xticklabels(rtts)
ax.plot(easy, marker='o', color='b', label=headers[1])
ax.plot(medium, marker='^', color='g', label=headers[2])
ax.plot(hard, marker='s', color='r', label=headers[3])
ax.set_ylim([0, 55])
ax.set(xlabel='Network round-trip-time (ms)')
ax.set(ylabel='Mean APE (cm)')
# ax.xaxis.label.set_size(label_font_size)
# ax.yaxis.label.set_size(label_font_size)
ax.legend(prop={'size': label_font_size})

plt.grid()
ax.set_axisbelow(True)

plt.savefig('latency_ape.pdf', bbox_inches='tight')

# show plot
plt.show()

