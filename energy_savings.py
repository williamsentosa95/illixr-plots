# Import libraries
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager

BASE_SZ = 11
TEXT_COLOR = '#202020'

label_font_size = 10
hatches = ['', "/", "xx", ""]

colors = ["cadetblue", "burlywood", "lightgreen", "plum", "indianred"]

def config_style():
    mpl.rcParams.update({'font.size': 11})

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
data_path_no_offload = "data/energy_no_offload.csv"
data_path_offload = "data/energy_offload.csv"

fig.set_size_inches(7, 5)

x_labels = []
data = []

textfile = open(data_path_no_offload, "r")
line_num = 1
components = []
headers = []

for line in textfile:
    if (line_num == 1):
        headers = line.strip('\n').split(',')
        x_labels = headers[1:]
    else:  
        entries = line.strip().split(",")
        components.append(entries[0])
        data_point = [round(float(i), 2) for i in entries[1:]]
        data.append(data_point)
    line_num += 1

x_labels2 = []
data2 = []

textfile = open(data_path_offload, "r")
line_num = 1
components2 = []

for line in textfile:
    if (line_num == 1):
        headers = line.strip('\n').split(',')
        x_labels2 = headers[1:]
    else:  
        entries = line.strip().split(",")
        components2.append(entries[0])
        data_point = [round(float(i), 2) for i in entries[1:]]
        data2.append(data_point)
    line_num += 1

assert(len(components) == len(data))
assert(len(components2) == len(data2))

bottom_data = [0] * len(x_labels)

n = 2            
x = np.arange(len(x_labels))  # the label locations
width = 0.3  # the width of the bars

ax.bar(x - width / 2, [0,0,0], width, color="white", label="w/o offl.", edgecolor="black")
ax.bar(x - width / 2, [0,0,0], width, color="white", hatch="///" ,label="w/ offl.", edgecolor="black")

for i in range(0, len(components)):
    result = ax.bar(x - width / 2, data[i], width, label=components[i], bottom=bottom_data, color=colors[i], edgecolor="black", zorder=3)
    for j in range(0, len(data[i])):
        bottom_data[j] += data[i][j]
    # if (i == len(components) - 1):
    #     ax.bar_label(result, padding=3)

print(x_labels2)
bottom_data2 = [0] * len(x_labels2)

for i in range(0, len(components2)):
    result = ax.bar(x + width / 2, data2[i], width, bottom=bottom_data2, color=colors[i], edgecolor="black", hatch="//", zorder=3)
    for j in range(0, len(data2[i])):
        bottom_data2[j] += data2[i][j]
    if (i == len(components2) - 1):
        power_reduction = []
        for k in range(0, len(bottom_data)):
            reduction = ((bottom_data[k] - bottom_data2[k]) / bottom_data[k]) * 100
            power_reduction.append(str(round(reduction, 1)) + "%")
        ax.bar_label(result, labels=power_reduction, padding=3, color="b", weight='bold')




ax.set_xticks(range(len(x_labels)))
ax.set_xticklabels(x_labels)
ax.set_ylim([0, 20])
ax.legend(loc='upper right', ncol=4)
ax.grid(zorder=0, axis='y')

ax.set_ylabel('Energy (W)')

plt.savefig('energy.pdf', bbox_inches='tight')

plt.show()