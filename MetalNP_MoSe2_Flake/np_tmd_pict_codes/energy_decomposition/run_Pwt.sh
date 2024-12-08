#!/bin/bash
#SBATCH --job-name=hc
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH -t 1200:00:00
##SBATCH --partition=LocalQ
#SBATCH --mem=20GB

cd $SLURM_SUBMIT_DIR

DPATH1=data
DPATH2=plots

time='0 5000 10000 15000 20000 25000 30000 55000 60000'

#mpirun -np 1  python3 src/pwt_eh.py $DPATH1/td-z-RPA/pulse/hcdist_nonresonant.npz $DPATH2/Pwt_eh_nonresonant.png >& log_pwteh_nonres
#mpirun -np 1  python3 src/pwt_eh.py $DPATH1/td-z-RPA/pulse/hcdist_resonant.npz $DPATH2/Pwt_eh_resonant.png >& log_pwteh_res
#
#mpirun -np 1  python3 src/pwt.py $DPATH1/td-z-RPA/pulse/transp_nonresonant.npz $DPATH2/Pwt_nonresonant.png >& log_pwt_nonres
#mpirun -np 1  python3 src/pwt.py $DPATH1/td-z-RPA/pulse/transp_resonant.npz $DPATH2/Pwt_resonant.png >& log_pwt_res

#mpirun -np 1  python3 src/jdos.py $DPATH1/td-z-RPA/pulse/transp_nonresonant.npz $DPATH2/jdos.dat
#mpirun -np 1  python3 src/jdos_eh.py $DPATH1/td-z-RPA/pulse/transp_nonresonant.npz $DPATH2/jdos_eh.dat

#for t in $time
#do
#     mpirun -np 1  python3 src/pw.py $DPATH1/td-z-RPA/pulse/transp_nonresonant.npz $DPATH2/Pw_nonresonant_$t.dat --time $t
#     mpirun -np 1  python3 src/pw.py $DPATH1/td-z-RPA/pulse/transp_resonant.npz $DPATH2/Pw_resonant_$t.dat --time $t
#done
