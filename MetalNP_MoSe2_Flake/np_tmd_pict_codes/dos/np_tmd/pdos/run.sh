#!/bin/bash
#SBATCH --job-name=pdos
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH -t 1200:00:00
##SBATCH --partition=LocalQ
#SBATCH --mem=20GB

cd $SLURM_SUBMIT_DIR

mpirun -np 1 python3 pdos.py >& pdos.log
