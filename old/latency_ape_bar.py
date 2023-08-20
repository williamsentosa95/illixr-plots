# Import libraries
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager

BASE_SZ = 14
TEXT_COLOR = '#202020'

label_font_size = 10
hatches = ['', "/", "xx", "o"]

colors = ["cadetblue", "burlywood", "indianred", "white"]

def config_style():
    mpl.rcParams.update({'font.size': label_font_size})

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


fig, axs = plt.subplots(2, 1)
data_path = "data/latency_ate_bar.txt"
data_path_2 = "data/latency_are_bar.txt"

fig.set_size_inches(6, 4)

line_num = 1

x_labels = []
labels = []

data = []

textfile = open(data_path, "r")

for line in textfile:
    if (line_num == 1):
        headers = line.strip('\n').split('\t')
        x_labels = headers[1:]
    else:  
        entries = line.strip().split("\t")
        labels.append(entries[0])
        data_point = [float(i) for i in entries[1:]]
        data.append(data_point)
    line_num += 1
            
x = np.arange(len(x_labels))  # the label locations
w = 0.18  # the width of the bars
n = len(labels)

# Creating plot
axs[0].set_xticks(range(len(x_labels)))
axs[0].set_xticklabels(x_labels)

for i in range(0, len(data)):
    position = x + (w*(1-n)/2) + i*w
    if (i < len(data) - 1):
        result = axs[0].bar(position, data[i], w, label=labels[i], color=colors[i], edgecolor="black", hatch=hatches[i])
    else:
        result = axs[0].bar(position, data[i], w, color=colors[i], edgecolor="black", hatch=hatches[i])
    # ax.bar_label(result, padding=0)

axs[0].set_ylim([0, 12])
axs[0].set(ylabel='Mean ATE (cm)')
axs[0].set(xlabel='Network RTT (ms)')
axs[0].yaxis.set_label_coords(-.08, .5)

axs[0].xaxis.label.set_size(label_font_size)
axs[0].yaxis.label.set_size(label_font_size)
axs[0].legend(prop={'size': label_font_size}, ncol=3)


axs[0].grid(axis='y')


axs[0].text(8.5, -0.5, "__", fontsize=30, color="red")

textfile = open(data_path_2, "r")
line_num = 1

x_labels = []
labels = []

data = []

for line in textfile:
    if (line_num == 1):
        headers = line.strip('\n').split('\t')
        x_labels = headers[1:]
    else:  
        entries = line.strip().split("\t")
        labels.append(entries[0])
        data_point = [float(i) for i in entries[1:]]
        data.append(data_point)
    line_num += 1


x = np.arange(len(x_labels))  # the label locations
n = len(labels)

# Creating plot
axs[1].set_xticks(range(len(x_labels)))
axs[1].set_xticklabels(x_labels)

for i in range(0, len(data)):
    position = x + (w*(1-n)/2) + i*w
    if (i == len(data) - 1):
        result = axs[1].bar(position, data[i], w, label=labels[i], color=colors[i], edgecolor="black", hatch=hatches[i])
    else:
        result = axs[1].bar(position, data[i], w, color=colors[i], edgecolor="black", hatch=hatches[i])
    # ax.bar_label(result, padding=0)

# ax.set_ylim([0, 2])
axs[1].set(ylabel='Mean ATE (degree)')
axs[1].set(xlabel='Network RTT (ms)')
axs[1].yaxis.set_label_coords(-.08, .5)

axs[1].xaxis.label.set_size(label_font_size)
axs[1].yaxis.label.set_size(label_font_size)
axs[1].legend(prop={'size': label_font_size})


axs[1].grid(axis='y')

axs[1].text(8.5, -0.5, "__", fontsize=30, color="red")

plt.savefig('latency_ape_bar.pdf', bbox_inches='tight')

# show plot
plt.show()

