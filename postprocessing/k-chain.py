import matplotlib
from matplotlib import rc
import matplotlib.pyplot as plt
import numpy as np
from numpy import loadtxt
from scipy.stats import gaussian_kde

rc('text',usetex=True)
font={'family' : 'normal',
    'weight' : 'normal',
    'size' :14}
matplotlib.rc('font',**font)

#dataFile = "../inputs/info.txt"
#info = loadtxt(dataFile,comments="%")
#n_S = int(info[0])
#n_s = int(info[1])
#n_phis_cal = int(info[2])
#n_phis_val = int(info[3])
#n_times = int(info[4])
#var = float(info[5])
#inad_type = int(info[6])
var = 100
inad_type = 1
n_s = 7
dim = n_s + 1

if inad_type == 1:
    pf = 2
elif inad_type == 2:
    pf = 4
elif inad_type == 3:
    pf = 2*n_s

dataFile = "sip_filtered_chain.dat"
# dataFile = "sip_raw_chain.dat"
c = loadtxt(dataFile,comments="%")
print(c.shape)
# c = -np.exp(c)
points = range(0,pf*n_s)
for p in points:
  plt.figure(p)
  plt.plot(c[:,p])
  print("p = ")
  print(p)
  print(" and mean = ")
  print(np.mean(c[:,p]))
  #plt.ylabel(r'need label here')
  #plt.savefig('plots/chains/chain.pdf')

  plt.show()
