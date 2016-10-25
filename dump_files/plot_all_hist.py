import numpy as np
import matplotlib.pyplot as plt

namelist = np.arange(1.15,1.405,0.025)
namelist = [-0.72,-0.68,-0.65]
namelist = [-0.726]
bins = np.linspace(-0.70, 1.70, 400)
bins_OG = bins[1:] * 0.5 + bins[:-1] * 0.5

N_sims = len(namelist)
color = iter(plt.cm.copper(np.linspace(0,1,N_sims)))
plt.figure(0)

k = 20000.0
temp = 340.0

# spatially average angles at every timestep to plot <theta_z>
for i in namelist:
    c = next(color)
    data = np.genfromtxt('/home/pratima/Biased-PeriodicLigand/dump_files/theta' + str(i) + '.txt', delimiter=' ')
    data = np.mean(data.reshape((-1, 240)), axis=1)
    total_prob, bins = np.histogram(data, bins=bins, density=True)

    theta = i 
    print theta, np.mean(data), np.std(data)
#     plt.plot(bins_OG*180.0/np.pi, total_prob, color=c, label="centred at theta = %3.3f" %theta)
    plt.plot(bins_OG*180.0/np.pi, total_prob, color=c, label="centred at theta = %3.1f" %(-theta*180.0/np.pi), linewidth=1)
    plt.vlines(-theta*180.0/np.pi, 0, 20, color=c, linewidth=2, linestyle='--', alpha=0.6)
    
eq_data = np.genfromtxt('/home/pratima/Biased-PeriodicLigand/dump_files/zangle_distr_top.340', delimiter=' ')
eq_data = -eq_data * np.pi / 180.0
eq_data = np.mean(eq_data.reshape((-1, 240)), axis=1)
eq_prob, bins = np.histogram(eq_data, bins = bins, density=True)
print np.mean(eq_data), np.std(eq_data)
plt.plot(bins_OG, eq_prob*180/np.pi, color='blue', linewidth=1, label='eqlbm')

plt.legend(loc='upper left')
plt.show()

# plot raw histogram without averaging spatially
color = iter(plt.cm.copper(np.linspace(0,1,N_sims)))
for i in namelist:
    c = next(color)
    data = np.genfromtxt('/home/pratima/Biased-PeriodicLigand/dump_files/theta' + str(i) + '.txt', delimiter=' ')
    print [ (itr_where % 240, itr_where/240) for itr_where in np.where(data < -1.0)[0] ]
    total_prob, bins = np.histogram(data, bins=bins, density=True)

    theta = i 
    print theta, np.mean(data), np.std(data)
#     plt.plot(bins_OG*180.0/np.pi, total_prob, color=c, label="centred at theta = %3.3f" %theta)
    plt.plot(bins_OG, total_prob, color=c, label="centred at theta = %3.1f" %(-theta*180.0/np.pi), linewidth=1)
    plt.vlines(-theta, 0, 3, color=c, linewidth=2, linestyle='--', alpha=0.6)

# eq_data=np.genfromtxt()

plt.legend(loc='upper left')
plt.show()

