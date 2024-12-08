import os
import sys
from pathlib import Path
import numpy as np
from gpaw.tddft.units import au_to_fs
import matplotlib.pyplot as plt
from numba import njit, prange

def gauss_iaw(energy, energy_i, energy_a, sigma):
    denergy_iaw = energy - energy_a - energy_i
    norm = 1.0 / (sigma * np.sqrt(2 * np.pi))
    giaw = norm * np.exp(-0.5 * denergy_iaw**2 / sigma**2)
    return giaw

def calc_jdos(transp_fpath, out_fpath):
    transp = np.load(transp_fpath)
    file_output = open(out_fpath, "w")

    energy_i = transp["energy_i"]
    energy_a = transp["energy_a"]

    sigma = 0.07 # broadening in eV

    energy = np.arange(-5, 5, 0.01)
    
    jdos = np.zeros(len(energy))
    
    for w in prange(len(energy)):
        sum = 0
        for a in range(len(energy_a)):
            for i in range(len(energy_i)):
                sum += gauss_iaw(energy[w], energy_i[i], energy_a[a], sigma)
        jdos[w] = sum

    file_output = open(out_fpath, "w")

    file_output.write("# Joint DOS\n")
    file_output.write(f"#  energy          jdos(w)\n")

    for w in prange(len(energy)):
        file_output.write(str(energy[w])+"       "+str(jdos[w])+"\n")

    file_output.close()


if __name__ == '__main__':
    import argparse
    from argparse_util import ExistingPathType, FilePathType, IntOrStrType

    parser = argparse.ArgumentParser()
    parser.add_argument('transp_fpath', type=FilePathType)
    parser.add_argument('out_fpath', type=FilePathType)

    args = parser.parse_args()

    calc_jdos(args.transp_fpath, args.out_fpath)
