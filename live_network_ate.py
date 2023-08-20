# Import libraries
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager
import csv

BASE_SZ = 18
TEXT_COLOR = '#202020'

label_font_size = 10
axis_label_font_size = 10

colors = ["indianred","burlywood", "cadetblue"]

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


fig, axs = plt.subplots(2, 1)
data_path_1 = "data/live_network_ate_cm.csv"
data_path_2 = "data/live_network_ate_degree.csv"

fig.set_size_inches(6, 5)


####### Process data_path_1 ##########

datapoints = []
headers = []
line_num = 1

textfile = open(data_path_1, "r")

for line in textfile:
    if (line_num == 1): # process the header
        headers = line.strip('\n').split(',')
    else:
        entries = [i for i in line.strip('\n').split(',')]  
        if (len(datapoints) == 0):
            for i in range(0, len(entries)):
                datapoints.append([])
        for i in range(0, len(entries)):
            datapoints[i].append(entries[i])
    line_num += 1

######### Process data_path_2 ##############

datapoints2 = []
headers2 = []
line_num = 1

textfile = open(data_path_2, "r")

for line in textfile:
    if (line_num == 1): # process the header
        headers2 = line.strip('\n').split(',')
    else:
        entries = [i for i in line.strip('\n').split(',')]  
        if (len(datapoints2) == 0):
            for i in range(0, len(entries)):
                datapoints2.append([])
        for i in range(0, len(entries)):
            datapoints2[i].append(entries[i])
    line_num += 1

########## Creating plot #############


# axs[0].set_xticks(datapoints[0])
# print(datapoints[0])
# axs[0].set_xticklabels(datapoints[0])
x_labels = datapoints[0]
labels = headers[1:]

axs[0].set_xticks(range(len(x_labels)))
axs[0].set_xticklabels(x_labels)

print(x_labels)
x = np.arange(len(x_labels))  # the label locations
w = 0.15  # the width of the bars
n = len(labels)

for i in range(1, len(datapoints)):
    values = np.array(datapoints[i]).astype(np.float)
    position = (x-0.15) + (w*(1-n)/2) + i*w
    print(position)
    result = axs[0].bar(position, values, w, edgecolor="black", color=colors[i-1], label=labels[i - 1], zorder=3)
        


axs[0].set_ylim([0, 15])
# axs[0].set(xlabel='Network round-trip-time (ms)')
axs[0].set(ylabel='ATE (cm)')
axs[0].yaxis.label.set_size(axis_label_font_size)
axs[0].legend(prop={'size': label_font_size}, loc='upper right', ncol=3)
axs[0].grid(zorder=0)

########### Sub plot 2 #############

x_labels = datapoints2[0]
labels = headers2[1:]

axs[1].set_xticks(range(len(x_labels)))
axs[1].set_xticklabels(x_labels)

print(x_labels)
x = np.arange(len(x_labels))  # the label locations
w = 0.15  # the width of the bars
n = len(labels)

for i in range(1, len(datapoints2)):
    values = np.array(datapoints2[i]).astype(np.float)
    position = (x-0.15) + (w*(1-n)/2) + i*w
    result = axs[1].bar(position, values, w, edgecolor="black", color=colors[i-1], label=labels[i - 1], zorder=3)
        


axs[1].set_ylim([0, 6])
axs[1].set(xlabel='EuRoc MAV datasets')
axs[1].set(ylabel='ATE (degree)')
axs[1].yaxis.label.set_size(axis_label_font_size)
axs[1].legend(prop={'size': label_font_size}, loc='upper right', ncol=3)
axs[1].grid(zorder=0)

plt.savefig('live_network_ate.pdf', bbox_inches='tight')

# # show plot
plt.show()

