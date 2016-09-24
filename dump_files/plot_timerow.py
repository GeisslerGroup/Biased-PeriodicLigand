import numpy as np
import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description="")
parser.add_argument("-bias", type=str, help="bias value to analyse")
parser.add_argument("-clean", action='store_true', help="whether to clean data or not")
parser.add_argument("-row", choices=["x","z"], help="which directiion to average out")
args = parser.parse_args()

data = np.genfromtxt('/home/pratima/Biased-PeriodicLigand/dump_files/theta' + args.bias + '.txt', delimiter=' ')

data = data.reshape((-1,20,12))

if args.row == "x":
    mean_tz = np.mean(data, axis=1)
    max_val = max([max(row) for row in mean_tz])
    print max_val
    min_val = min([min(row) for row in mean_tz])
    mid = (max_val - min_val) * 0.5
    print min_val
    if args.clean:
        mean_tz[mean_tz < (min_val + 0.1)*np.pi/180.0] = mid*np.pi/180.0	# set disordered angles to mid_val
    # mean_tz = (mean_tz - min_val) / (max_val - min_val)
    mean_tz = np.transpose(mean_tz)
    
    plt.figure()
    plt.imshow(mean_tz, aspect=20, cmap="seismic", origin="lower")
    plt.yticks(np.arange(0, 13, 1))
    plt.ylim(-0.5,11.5)
    for i in np.arange(-0.5,12,0.5):
        plt.hlines(i, 0, 400, linestyle='solid', linewidth=2)
    plt.show()

if args.row == "z":
    mean_tx = np.mean(data, axis=2)
    max_val = max([max(row) for row in mean_tx])
    print max_val
    min_val = min([min(row) for row in mean_tx])
    mid = (max_val - min_val) * 0.5
    print min_val
    if args.clean:
        mean_tx[mean_tx < (min_val + 0.1)*np.pi/180.0] = mid*np.pi/180.0	# set disordered angles to mid_val
    mean_tx = np.transpose(mean_tx)
    
    plt.figure()
    plt.imshow(mean_tx, aspect=20, cmap="seismic", origin="lower")
    plt.yticks(np.arange(0, 21, 1))
    # plt.ylim(-0.5,20.5)
    for i in np.arange(-0.5,20,0.5):
        plt.hlines(i, 0, 400, linestyle='solid', linewidth=2)
    plt.show()

