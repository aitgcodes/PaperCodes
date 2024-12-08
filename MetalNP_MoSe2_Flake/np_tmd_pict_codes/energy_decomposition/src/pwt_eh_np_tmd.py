import os
import sys
from pathlib import Path
import numpy as np
from gpaw.tddft.units import au_to_fs
import matplotlib.pyplot as plt

def extract_pwt(hcdist_fpath, out_fpath):
    hcdist = np.load(hcdist_fpath)
    file_output = open(out_fpath, "w")

    time_t = hcdist["time_t"] /1000   # from as to fs
    energy_o = hcdist["energy_o"]
    energy_u = hcdist["energy_u"]

    dist_to = hcdist["dist_to"]
    dist_tu = hcdist["dist_tu"]

    # total P(w,t)
    en = []
    for i in range(len(energy_o)):
        en.append(energy_o[i])
    for i in range(len(energy_u)):
        en.append(energy_u[i])
    
    energy = np.array(en)

    Pwt = np.concatenate((dist_to, dist_tu), axis=1)

    t_new = np.arange(0, 6001, 250)

    Pwt_new = np.zeros([len(t_new), len(energy)])

    '''
      Taking all the time points takes much longer time and memory.
      To avoid this, the code below computed P(omega, t) with the intervals of 5 fs
      Note: Total simulation time: 120 fs. So, only 24 data points for time.
      It could be increased by taking 1 fs time interval.
      Also Note: 20 attoseconds time step was used in the simulations.
      250th point ==> 250 * 20 = 5000 as or 5 fs.
      To plot in fs, we multiply by 20 and divide by 1000 to time array.
    '''

    for t in range(len(t_new)):
        Pwt_new[t, :] = Pwt[250*t, :]

    t_new = t_new * 20 / 1000

    plt.rcParams["figure.figsize"] = [6.0, 6.0]
    plt.rcParams["figure.autolayout"] = True

    fig, ax = plt.subplots()
    ax.set_title(r'Ag$_{55}$', size=20)
    levels = 50
    #ct = ax.contourf(time_t, energy, Pwt.T, cmap="viridis", levels=levels)
    ct = ax.contourf(t_new, energy, Pwt_new.T, cmap="viridis", levels=levels)
    ax.set_xlabel('Time (fs)', fontsize = 20.0)
    ax.set_ylabel('Kohn-Sham energy (eV)', fontsize = 20.0)
    ax.set_xlim(0, 120)
    ax.set_xticks(range(0, 121, 20))
    ax.tick_params(axis='both', which='major', labelsize=15)
    cbar = fig.colorbar(ct, ax=ax)
    cbar.ax.tick_params(axis='y', direction='in', length=8, labelsize=12)
    cbar.set_label(r"P($\varepsilon$, t)", fontsize = 20)
    fig.savefig(out_fpath) 

if __name__ == '__main__':
    import argparse
    from argparse_util import ExistingPathType, FilePathType, IntOrStrType

    parser = argparse.ArgumentParser()
    parser.add_argument('hcdist_fpath', type=FilePathType)
    parser.add_argument('out_fpath', type=FilePathType)

    args = parser.parse_args()

    extract_pwt(args.hcdist_fpath, args.out_fpath)
