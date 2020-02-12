import matplotlib
from matplotlib import rc
import matplotlib.pyplot as plt
import numpy as np
from numpy import loadtxt
from scipy.interpolate import interp1d
from operator import add
from operator import sub
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes


rc('text',usetex=True)
font={'family' : 'serif',
    'weight' : 'normal',
    'size' :16}
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

# var = 4000
n_s = 7
dim = n_s +1
n_weeks = 52

dataFile = "../inputs/data.txt"; data = loadtxt(dataFile,comments="%")
print(data)
print(data.shape)
times = np.linspace(1,52,52,endpoint=True)
state = np.linspace(1,52,52,endpoint=True)
#rep_factor = 10./9;
rep_factor = 2.;
state[0] = rep_factor* data[0,1]
for i in range(1,len(state)):
    state[i] = state[i-1] + rep_factor * data[i,1];

#print(state)

dataFile = "../inputs/data-red.txt"
data = loadtxt(dataFile,comments="%")
red = data[7:417:8,2]
#print(red)
#print(red.shape)

dataFile = "qoi-stats-rep50p"
q = loadtxt(dataFile,comments="%")

# spec_names = ('H$_2$', 'O$_2$', 'H', 'O', 'OH', 'HO$_2$', 'H$_2$O', 'H$_2$O$_2$',
#     'N$_2$', 'Temperature')

# sigma = np.sqrt(var)
# err = np.random.normal(0,sigma,n_times)
# state = state + err
# state[np.where(state<0)] = 0
# ylabel = ' [mol/m$^3$]'
rmean = [];
r1 = []; r2 = []; r3 = []; r4 = [];
for j in range(0,n_weeks):
  rmean.append(q[j*dim+7,0])
  r1.append(q[j*dim+7,1])
  r2.append(q[j*dim+7,2])
  r3.append(q[j*dim+7,3])
  r4.append(q[j*dim+7,4])

fig, ax = plt.subplots()
#ax.plot(times,state,'^',color='C0',markersize=7,label='Data')
ax.plot(times,state,'^',color='C0',markersize=7,label='Modified data, with 50\% under-reporting')
ax.fill_between(times,r2,r3,facecolor='C3',alpha=.4)
ax.fill_between(times,r1,r4,facecolor='C3',alpha=.1)
ax.plot(times,rmean,color='C3',linewidth=2,label='Enriched model')
# print(datatimes)
# print(times)
#red = interp1d(datatimes,state_red)
#plt.plot(times,red(times),'g', linewidth=2,label='Reduced model')
#plt.plot(times,red, linewidth=2,label='Reduced model')


plt.xlabel('Epidemiological week')
plt.ylabel('Cummulative number of cases')
plt.ticklabel_format(axis='y',style='sci',scilimits=(3,0))
plt.tight_layout()
#if k < n_phis_cal:
 # plt.title('Calibration scenario '+str(k+1)+' of '+str(n_phis_cal))
#else:
 # plt.title('Prediction scenario '+str(k+1-n_phis_cal)+' of '+str(n_phis_val))

#plt.ylabel('$x_{}$'.format(i+1),fontsize=28)
#plt.xlim(times[0],times[-1])
ax.locator_params(nbins=10)
ax.legend(loc=0)
# plt.show()
# plt.savefig('red-plots/smooth-'
#         '%s' '-' '%s''.pdf' %(k,i))
# plt.savefig('red-plots/smooth-pred-'
#        '%s' '-' '%s''.pdf' %(k,i))


# ZOOM
axins = zoomed_inset_axes(ax,1.4, loc='center right')
# replot what we need for zoom
axins.plot(times,state,'^',color='C0',markersize=7,label='Data')#, with 50\% under-reporting')
axins.fill_between(times,r2,r3,facecolor='C3',alpha=.4)
axins.fill_between(times,r1,r4,facecolor='C3',alpha=.1)
axins.plot(times,rmean,color='C3',linewidth=2,label='Enriched model')
# set zoom limits
#x1, x2, y1, y2 = 12, 30, 175000, 300000
x1, x2, y1, y2 = 12, 30, 320000, 550000
axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)
plt.xticks(visible=False)
plt.yticks(visible=False)

from mpl_toolkits.axes_grid1.inset_locator import mark_inset
mark_inset(ax, axins, loc1=1, loc2=3, fc="none", ec="0.5")

plt.savefig('/users/rebeccam/repos/documents/papers/zika-discrepancy/rawfigs/zika-rep50p.pdf')
plt.show()
