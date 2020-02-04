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
for i in range(0,len(state)):
   # state[i] = state[i-1] + data[i];
    state[i] = data[i];
  #  mod_state[i] = state[i]*reporting_factor

#print(state)

# reduced model with nominal parameters
dataFile = "../inputs/data-red.txt"
data = loadtxt(dataFile,comments="%")
print(data.shape)
#pick out every 8th species
nom = data[7:417:8,2]
print(nom.shape)
#print(red)
#print(red.shape)

# reduced model from Americo with nominal params
dataFile = "AMC_table1C.txt"
data = loadtxt(dataFile,delimiter=",",comments="%")
print(data.shape)
#pick out every 7th day
cal1 = data[0:417:7]

# reduced model from Americo with calibrated params
dataFile = "AMC_table2C.txt"
data = loadtxt(dataFile,delimiter=",",comments="%")
print(data.shape)
#pick out every 7th day
cal2 = data[0:417:7]

dataFile = "../postprocessing/qoi-stats-enr"
q = loadtxt(dataFile,comments="%")

# spec_names = ('H$_2$', 'O$_2$', 'H', 'O', 'OH', 'HO$_2$', 'H$_2$O', 'H$_2$O$_2$',
#     'N$_2$', 'Temperature')

sigma = np.sqrt(var)
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

s1 = []; s2 = []; s3 = []; s4 = [];
for j in range(0,n_weeks):
  s1.append(0.95*q[j*dim+7,0])
  s2.append(0.975*q[j*dim+7,0])
  s3.append(1.025*q[j*dim+7,0])
  s4.append(1.05*q[j*dim+7,0])

fig, ax = plt.subplots()
ax.plot(times,state,'^',markersize=7,color='C0',label='Data')
#ax.plot(times,nom,linewidth=2,color='C1',label='Reduced model, nominal parameters')
#ax.plot(times,cal1,linewidth=2,color='C2',label='Reduced model, first calibration')
#ax.plot(times,cal2,linewidth=2,color='C4',label='Reduced model, second calibration')
ax.plot(times,rmean,linewidth=2,color='C3',label='Enriched model')
ax.fill_between(times,r2,r3,facecolor='C3',alpha=.6)
ax.fill_between(times,r1,r4,facecolor='C3',alpha=.3)
#plt.fill_between(times,s2,s3,facecolor='C3',alpha=.3)
#plt.fill_between(times,s1,s4,facecolor='C3',alpha=.1)
# print(datatimes)
# print(times)
#red = interp1d(datatimes,state_red)
#plt.plot(times,red(times),'g', linewidth=2,label='Reduced model')
#plt.plot(times,red,'g', linewidth=2,label='Reduced model')

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



# ZOOM
axins = zoomed_inset_axes(ax,1.4, loc='center right')
# replot what we need for zoom
axins.plot(times,state,'^',color='C0',markersize=7,label='Data')#, with 50\% under-reporting')
axins.fill_between(times,r2,r3,facecolor='C3',alpha=.6)
axins.fill_between(times,r1,r4,facecolor='C3',alpha=.3)
axins.plot(times,rmean,color='C3',linewidth=2,label='Enriched model')
# set zoom limits
x1, x2, y1, y2 = 12, 30, 150000, 275000
axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)
plt.xticks(visible=False)
plt.yticks(visible=False)

from mpl_toolkits.axes_grid1.inset_locator import mark_inset
mark_inset(ax, axins, loc1=1, loc2=3, fc="none", ec="0.5")





plt.savefig('/users/rebeccam/repos/documents/papers/zika-discrepancy/rawfigs/zika-enr.pdf')
# plt.savefig('red-plots/smooth-'
#         '%s' '-' '%s''.pdf' %(k,i))
# plt.savefig('red-plots/smooth-pred-'
#        '%s' '-' '%s''.pdf' %(k,i))

plt.show()
