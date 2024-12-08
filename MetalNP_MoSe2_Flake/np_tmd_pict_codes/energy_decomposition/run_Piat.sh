#!/bin/bash
#SBATCH --job-name=hc
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH -t 1200:00:00
##SBATCH --partition=LocalQ
#SBATCH --mem=20GB

cd $SLURM_SUBMIT_DIR

DPATH=data


export START_TIME=`date +%s.%3N`
export TIME_LIMIT=`squeue -h -o %L -j $SLURM_JOB_ID`

# Calculate Pia(t)
mpirun -np 1  python3 src/pulse_transp_Pia.py $DPATH/{unocc/{unocc.gpw,ksd.ulm},td-z-RPA/pulse/{pulse.pickle,rho,transp_all.npz}}  --maxtime 120e3 --transitions all
mpirun -np 1  python3 src/pulse_transp_Pia.py $DPATH/{unocc/{unocc.gpw,ksd.ulm},td-z-RPA/pulse/{pulse.pickle,rho,transp_resonant.npz}}  --maxtime 120e3 --transitions resonant
mpirun -np 1  python3 src/pulse_transp_Pia.py $DPATH/{unocc/{unocc.gpw,ksd.ulm},td-z-RPA/pulse/{pulse.pickle,rho,transp_nonresonant.npz}}  --maxtime 120e3 --transitions nonresonant
