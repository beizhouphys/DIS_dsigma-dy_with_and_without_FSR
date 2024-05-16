#!/usr/bin/python
from numpy import *
import matplotlib.pyplot as plt
from scipy import integrate


energies = array([
    #1.e+03,
    1.e+04,
    #1.e+07,
    1.e+09,
    #1.e+11
    ])

Enus_str = [
        #'1E+03',
        '1E+04',
        #'1E+07',
        '1E+09',
        #'1E+11',
        ]


directory_FSR   = "with_FSR/numu_numubar/"
directory_noFSR = 'without_FSR/'


from matplotlib import gridspec
fig = plt.figure(figsize=(10, 8), facecolor='w')
gs = gridspec.GridSpec(2, 1, height_ratios=[2, 1])
ax = plt.subplot(gs[0]); ax1 = plt.subplot(gs[1])
plt.subplots_adjust(left=0.125, bottom=0.1, right=0.95, top=0.95, wspace=0.03, hspace=0.05)

ax.set_xscale('log');  ax.set_yscale('log')
ax1.set_xscale('log'); ax1.set_yscale('linear')

for i in range(len(energies)):
    filename_nu  = f"{directory_FSR}factors_CT18sub_A2Z1_set000_Enu{energies[i]:.0e}GeV_CC_neu.txt"
    #filename_ant = f"{directory_FSR}factors_CT18sub_A2Z1_set000_Enu{energies[i]:.0e}GeV_CC_ant.txt"
    
    data_nu  = loadtxt(filename_nu).T
    plot = ax1.plot(data_nu[0], data_nu[1], '--', label='Enu={:.1e} GeV'.format(energies[i]), lw=1.5, ms=2)
    clr = plot[0].get_color()

    tmp = loadtxt(directory_noFSR+'CT18sub_A2Z1_set000_Enu'+Enus_str[i]+'GeV_CC_neu.txt', skiprows=0).T
    norm = integrate.simps( tmp[1], tmp[0] )
    ax.plot( tmp[0], tmp[0]*tmp[1]/norm, '-', label=r'$E_\nu$ = '+'{:.1e} GeV'.format(energies[i]), color=clr, lw=1.5, ms=2.5) 
    ax.plot( tmp[0], tmp[0]*tmp[1]/norm*(1+data_nu[1]), '--', color=clr, lw=1.5, ms=2.5) 

    print( tmp[0]==data_nu[0] )
ax.plot( [10,100], [1,2], 'k-',  label=r'Without radiative correction', lw=1.5, ms=2.5) 
ax.plot( [10,100], [1,2], 'k--', label=r'With radiative correction', lw=1.5, ms=2.5) 


ax. set_xlim(1e-4, 1); 
ax1.set_xlim(1e-4, 1)
ax. set_ylim(1e-5, 1)
ax1.set_ylim(-0.5, 0.5)
ax1.set_xlabel(r"$y$",fontsize=20, labelpad=None) #
ax. set_ylabel(r"$y \times \frac{1}{\sigma} d\sigma/dy$",fontsize=20)
ax1.set_ylabel(r"$\frac{d\sigma^{(1)}/dy}{d\sigma^{(0)}/dy}$",fontsize=20)
ax.legend(loc='best',prop={'size':18})

ax.set_xticklabels([]) # remove the tick numbers on the x axis of the upper subplot
ax1.yaxis.get_ticklocs(minor=True)
ax1.minorticks_on()

ax.tick_params(axis='both', which='major', direction='in', length = 10, width = 1.5, labelsize=22, right=True, top=True)
ax.tick_params(axis='x', pad=6) # for numbers with superscript, 6 is from adjusting to match y axis
ax.tick_params(axis='both', which='minor', direction='in', length = 5., width = 1.0, labelsize=22, right=True, top=True)
ax1.tick_params(axis='both', which='major', direction='in', length = 10, width = 1.5, labelsize=22, right=True, top=True)
ax1.tick_params(axis='x', pad=6) # for numbers with superscript, 6 is from adjusting to match y axis
ax1.tick_params(axis='both', which='minor', direction='in', length = 5., width = 1.0, labelsize=22, right=True, top=True)

plt.grid()
for axis in ['top','bottom','left','right']:
    ax1.spines[axis].set_linewidth(1.5)
    ax.spines[axis].set_linewidth(1.5)
plt.show()



#backup
