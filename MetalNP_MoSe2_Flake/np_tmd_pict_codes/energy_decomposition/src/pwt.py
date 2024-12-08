import os
import sys
from pathlib import Path
import numpy as np
from gpaw.tddft.units import au_to_fs
import matplotlib.pyplot as plt
from numba import njit, prange

def gauss_iaw(energy, energy_i, energy_a, sigma):
    denergy_iaw = energy - (energy_a - energy_i)
    norm = 1.0 / (sigma * np.sqrt(2 * np.pi))
    giaw = norm * np.exp(-0.5 * denergy_iaw**2 / sigma**2)
    return giaw

def calc_pwt(transp_fpath, out_fpath):
    transp = np.load(transp_fpath)
    file_output = open(out_fpath, "w")

    time_t = transp["time_t"] /1000   # from as to fs
    energy_i = transp["energy_i"]
    energy_a = transp["energy_a"]

    Pia_t = transp["transp"]

    sigma = 0.07 # broadening in eV

    energy = np.arange(0, 5, 0.1)

    ''' Create a new time grid to select the time
        in steps of 5 fs. 

        Taking all the time points takes much longer time and memory.
        To avoid this, the code below computed P(omega, t) with the intervals of 5 fs
        Note: Total simulation time: 120 fs. So, only 24 data points for time.
        It could be increased by taking 1 fs time interval.
        Also Note: 20 attoseconds time step was used in the simulations.
        250th point ==> 250 * 20 = 5000 as or 5 fs.
        To plot in fs, we multiply by 20 and divide by 1000 to time array.
    '''

    t_new = np.arange(0, 6001, 250)

    Pwt = np.zeros([len(t_new), len(energy)])
    
    for t in range(len(t_new)):
        for w in prange(len(energy)):
            for a in range(len(energy_a)):
                for i in range(len(energy_i)):
                    giaw = gauss_iaw(energy[w], energy_i[i], energy_a[a], sigma)
                    Pwt[t, w] +=  Pia_t[250*t, i, a] * giaw

    plt.rcParams["figure.figsize"] = [6.0, 6.0]
    plt.rcParams["figure.autolayout"] = True

    fig, ax = plt.subplots()
    ax.set_title(r'Ag$_{55}$', size=20)
    t_new = t_new * 20 / 1000
    
    ct = ax.contourf(t_new, energy, Pwt.T, cmap="viridis", levels=50)
    
    ax.set_xlabel('Time (fs)', fontsize = 20.0)
    ax.set_ylabel(' Energy (eV)', fontsize = 20.0)
    ax.set_xlim(0, 120)
    ax.set_xticks(range(0, 121, 20))
    ax.tick_params(axis='both', which='major', labelsize=15)
    cbar = fig.colorbar(ct, ax=ax)
    cbar.ax.tick_params(axis='y', direction='in', length=8, labelsize=12)
    cbar.set_label(r"P($\omega$, t)", fontsize = 20)
    fig.savefig(out_fpath) 

if __name__ == '__main__':
    import argparse
    from argparse_util import ExistingPathType, FilePathType, IntOrStrType

    parser = argparse.ArgumentParser()
    parser.add_argument('transp_fpath', type=FilePathType)
    parser.add_argument('out_fpath', type=FilePathType)

    args = parser.parse_args()

    calc_pwt(args.transp_fpath, args.out_fpath)
