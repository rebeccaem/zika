import matplotlib
from matplotlib import rc
import matplotlib.pyplot as plt
import numpy as np
from numpy import loadtxt
from scipy.interpolate import interp1d
from operator import add
from operator import sub

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
#var = int(info[5])
#inad_type = int(info[6])

var = 100
n_s = 7
dim = n_s +1
n_weeks = 52

dataFile = "AMC_dataC.txt"
data = loadtxt(dataFile,delimiter=",",comments="%")
print(data)
print(data.shape)
times = np.linspace(1,52,52,endpoint=True)
state = np.linspace(1,52,52,endpoint=True)
mod_state = np.linspace(1,52,52,endpoint=True)
reporting_factor = 1.1
for i in range(1,len(state)):
   # state[i] = state[i-1] + data[i];
    state[i] = data[i];
  #  mod_state[i] = state[i]*reporting_factor

#print(state)

dataFile = "../inputs/data-red.txt"
data = loadtxt(dataFile,comments="%")
red = data[7:417:8,2]
#print(red)
#print(red.shape)

plt.figure()
plt.plot(times,red,'b',linewidth=2,label='Reduced model')
plt.plot(times,state,'r^',markersize=7,label='Data')
# print(datatimes)
# print(times)
#red = interp1d(datatimes,state_red)
#plt.plot(times,red(times),'g', linewidth=2,label='Reduced model')
#plt.plot(times,red,'g', linewidth=2,label='Reduced model')

plt.xlabel('Weeks')
plt.ylabel('Cummulative number of cases')
#if k < n_phis_cal:
 # plt.title('Calibration scenario '+str(k+1)+' of '+str(n_phis_cal))
#else:
 # plt.title('Prediction scenario '+str(k+1-n_phis_cal)+' of '+str(n_phis_val))

#plt.ylabel('$x_{}$'.format(i+1),fontsize=28)
#plt.xlim(times[0],times[-1])
plt.locator_params(nbins=5)
plt.legend(loc=0)
# plt.show()
#plt.savefig('/users/rebeccam/Documents/talks/2019/rawfigs/zika-red.pdf')
# plt.savefig('red-plots/smooth-'
#         '%s' '-' '%s''.pdf' %(k,i))
# plt.savefig('red-plots/smooth-pred-'
#        '%s' '-' '%s''.pdf' %(k,i))

plt.show()
