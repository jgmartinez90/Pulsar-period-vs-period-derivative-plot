#!/user/bin/python

import os.path
import glob

import subprocess
from matplotlib import pyplot as plt
import numpy as np
from math import pow, sqrt, log10
#from math import floor, pow, log10, exp, sqrt
import datetime as dt

from mpl_toolkits.mplot3d import Axes3D
from subprocess import Popen, PIPE, STDOUT, call

from collections import Counter
import matplotlib.cm as cm
from scipy import signal
from scipy import misc

from pylab import *


def magnetic_field_iso(B, P):
    magnetic_field_iso = pow(B, 2)/(pow(3.2 *pow(10,19),2) * np.array(P))
    return magnetic_field_iso

def age_iso(tau, P):
#    age_iso = P/(2*tau)
    age_iso = (15.8*pow(10,6)*P*pow(10,-15))/ tau
    return age_iso

def death_line(P):
    #death_line = 2 * death * P**3
    death_line = 10**(2*(43.8/4)) * (3.2e19**(-2.)) * (P**(2))
    #other_death_line = 10**(2*log10(P) - 16.52 + 6)
    return death_line
    #return other_death_line
    


co_p0 = []
he_p0 = []
ns_p0 = []
ul_p0 = []
ms_p0 = []
snr_p0 = []
co_p1 = []
he_p1 = []
ns_p1 = []
ul_p1 = []
ms_p1 = []
snr_p1 = []

f = open('PPdot_CO.txt', 'r')
for line in f:
    co_p0.append(float(line.rsplit(" ")[0]))
    co_p1.append(float(line.rsplit(" ")[2]))

f = open('PPdot_NS.txt', 'r')
for line in f:
    ns_p0.append(float(line.rsplit(" ")[0]))
    ns_p1.append(float(line.rsplit(" ")[2]))

f = open('PPdot_UL.txt', 'r')
for line in f:
    ul_p0.append(float(line.rsplit(" ")[0]))
    ul_p1.append(float(line.rsplit(" ")[2]))

f = open('PPdot_He.txt', 'r')
for line in f:
    he_p0.append(float(line.rsplit(" ")[0]))
    he_p1.append(float(line.rsplit(" ")[2]))
#    print he_p1

f = open('PPdot_SNR.txt', 'r')
for line in f:
    if line.split()[0] == '*' or line.split()[1] == '*' :
	print line.split()[0], line.split()[1]
    else:
	snr_p0.append(float(line.split()[0]))
    	print snr_p0
    	snr_p1.append(float(line.split()[1]))
    	print snr_p1

f = open('PPdot_Main.txt', 'r')
for line in f:
#    print line.split()[0]
    if line.split()[0] == '*' or line.split()[1] == '*' :
        print line.split()[0], line.split()[1]
    else:
        ms_p0.append(float(line.split()[0]))
        ms_p1.append(float(line.split()[1]))


P = np.linspace(pow(10, -3), 10,100  )

plt.figure(figsize=(8.1, 8.1))


ax = plt.figure(1)
ax = plt.subplot(111)

plt.plot(P, magnetic_field_iso(pow(10,8), P), 'k--', linewidth = 0.5)
plt.text(0.007, magnetic_field_iso(pow(10,8), 0.007), r"$10^{8} \mathrm{G}$", rotation = 340, color= 'k', fontsize= 13)
plt.plot(P, magnetic_field_iso(pow(10,9), P), 'k--', linewidth = 0.5)
plt.text(0.4, magnetic_field_iso(pow(10,9), 0.4), r"$10^{9} \mathrm{G}$", rotation = 340, color= 'k', fontsize= 13)
plt.plot(P, magnetic_field_iso(pow(10,10), P), 'k--', linewidth = 0.5)
plt.text(4, magnetic_field_iso(pow(10,10), 4), r"$10^{10} \mathrm{G}$", rotation = 340, color= 'k', fontsize= 13)
plt.plot(P, magnetic_field_iso(pow(10,11), P), 'k--', linewidth = 0.5)
plt.text(4, magnetic_field_iso(pow(10,11), 4), r"$10^{11} \mathrm{G}$", rotation = 340, color= 'k', fontsize= 13)
plt.plot(P, magnetic_field_iso(pow(10,12), P), 'k--', linewidth = 0.5)
plt.text(4, magnetic_field_iso(pow(10,12), 4), r"$10^{12} \mathrm{G}$", rotation = 340, color= 'k', fontsize= 13)
plt.plot(P, magnetic_field_iso(pow(10,13), P), 'k--', linewidth = 0.5)
plt.text(4, magnetic_field_iso(pow(10,13), 4), r"$10^{13} \mathrm{G}$", rotation = 340, color= 'k', fontsize= 13)
plt.plot(P, magnetic_field_iso(pow(10,14), P), 'k--', linewidth = 0.5)
plt.text(4, magnetic_field_iso(pow(10,14), 4), r"$10^{14} \mathrm{G}$", rotation = 340, color= 'k', fontsize= 13)

plt.plot(P, age_iso(pow(10,4), P), 'k--', linewidth = 0.5)
plt.text(0.0012, age_iso(pow(10,4), 0.0012), r"$10 \mathrm{Kyr}$", rotation = 17, color= 'k', fontsize= 13)
plt.plot(P, age_iso(pow(10,5), P), 'k--', linewidth = 0.5)
plt.text(0.0012, age_iso(pow(10,5), 0.0012), r"$100 \mathrm{Kyr}$", rotation = 17, color= 'k', fontsize= 13)
plt.plot(P, age_iso(pow(10,6), P), 'k--', linewidth = 0.5)
plt.text(0.0012, age_iso(pow(10,6), 0.0012), r"$1 \mathrm{Myr}$", rotation = 17, color= 'k', fontsize= 13)
plt.plot(P, age_iso(pow(10,7), P), 'k--', linewidth = 0.5)
plt.text(0.0012, age_iso(pow(10,7), 0.0012), r"$10 \mathrm{Myr}$", rotation = 17, color= 'k', fontsize= 13)
plt.plot(P, age_iso(pow(10,8), P), 'k--', linewidth = 0.5)
plt.text(0.0012, age_iso(pow(10,8), 0.0012), r"$100 \mathrm{Myr}$", rotation = 17, color= 'k', fontsize= 13)
plt.plot(P, age_iso(pow(10,9), P), 'k--', linewidth = 0.5)
plt.text(0.0012, age_iso(pow(10,9), 0.0012), r"$1 \mathrm{Gyr}$", rotation = 17, color= 'k', fontsize= 13)
plt.plot(P, age_iso(pow(10,10), P), 'k--', linewidth = 0.5)
plt.text(0.0011, age_iso(pow(10,10), 0.0011), r"$10 \mathrm{Gyr}$", rotation = 17, color= 'k', fontsize= 13)
plt.plot(P, death_line(P), 'k', linewidth = 1.5)
plt.text(0.02, death_line(0.03), r'$\mathrm{death\, line}$', rotation = 35, color= 'k', fontsize= 13)

plt.scatter(ms_p0, ms_p1, marker = ',', s = 6, label = 'Isolated')
plt.scatter(he_p0, he_p1, marker='o',  facecolors='b', edgecolors = 'r', s = 18, label ='WD companion')
plt.scatter(co_p0, co_p1, marker = 'o', facecolors='b', edgecolors='r', s = 18)
plt.scatter(ns_p0, ns_p1, marker = 'd', facecolors='goldenrod', edgecolors='darkgrey', s = 100, linewidth = 1, label = 'NS companion')
plt.scatter(ul_p0, ul_p1, c = 'k', marker= '^', s = 20, facecolors='g', edgecolors='g', linewidth = 3, label = 'Ultra light companion')
plt.scatter(snr_p0, snr_p1, marker = 'p',facecolors='lightskyblue', edgecolors= 'lightskyblue', s = 35, label = 'SNR Association')



plt.xlim(pow(10,-3), 10)
plt.ylim(0.5*pow(10,-21), pow(10, -9))

#ax.set_yticks([pow(10,-21), pow(10,-15), pow(10, -13)])
ax.set_yscale('log')
ax.set_xscale('log')
plt.yticks([pow(10,-21), pow(10,-19), pow(10,-17), pow(10,-15), pow(10,-13), pow(10,-11), pow(10,-9)], fontsize = 10)
ax.set_xticklabels(['0.0001','0.001', '0.01', '0.1', '1', '10'])
#ax.set_yticklabels(['-22','-21', '-20', '-19', '-18', '-17', '-16', '-15', '-14', '-13'], rotation='vertical')

ax.tick_params(axis='both', labelsize=15, pad=6)
ax.spines['top'].set_linewidth(1.6)
ax.spines['bottom'].set_linewidth(1.6)
ax.spines['left'].set_linewidth(1.6)
ax.spines['right'].set_linewidth(1.6)
ax.xaxis.set_tick_params(width=1.5)
ax.yaxis.set_tick_params(width=1.5)
ax.xaxis.labelpad = 10
ax.yaxis.labelpad = 10

handles, labels = ax.get_legend_handles_labels()

legend = ax.legend( loc =2, ncol=1, prop={'size': 12}, fancybox=False, shadow=False, borderpad=1, scatterpoints = 1)

legend.legendHandles[0]._sizes = [50]
legend.legendHandles[1]._sizes = [50]
legend.legendHandles[2]._sizes = [50]
legend.legendHandles[3]._sizes = [45]
legend.legendHandles[4]._sizes = [50]







plt.xlabel(r'Period (s)', fontsize=20)
plt.ylabel(r"Period derivative (s s$^{-1}$)" , fontsize=20)
plt.tight_layout()
plt.savefig('/homes/joey/Scripts/PPdot_diagram/PPdot_diagram_final.eps', dpi=100)
#plt.show()

