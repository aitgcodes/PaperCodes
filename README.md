## Plasmon Induced Charge Transfer Dynamics in Metallic Nanoparticle-MoSe2 Nanoﬂake Heterostructures
The project contains all the input files related to the work.

### The code structure of GPAW input files

    1. **rlx**: The directory contains the input files for geometry relaxation and to generate the trajectory file.
    
    2. **spectrum**: The directory contains the input files to obtain the photoabsorption spectrum, the induced density 
                     at a given frequency, the transition contribution map (TCM), and the generalized plasmonicity index (gpi).
                     The gpi sub-directory contains the codes to calculate the field enhancement, the induced potential, 
                     and the two-dimensional projection of the induced charge density for a list of frequencies.
                     
    3. **bader_analysis**: The directory contains the necessary scripts to calculate the ground state charge transfer using 
                           the Bader analysis.

    4. **dipole_moment**: This directory contains the input file to perform the time-dependent simulations using a 
                          Gaussian pulse and recording the time-dependent dipole moment.

    5. **dos**: The directory contains the scripts to calculate the density of states as well as the projected dos.

    6. **indden_t**: The python scripts to obtain the real-space version of the induced charge density as a function
                     of time using the time-dependent charge density in the electron-hole (ia, i -> occupied states, a -> unoccupied states) basis.

    7. **energy_decomposition**: This path contains all the scripts related to the hot-carrier analysis in terms of the energy decomposition
                                 and the plasmon-induced direct charge transfer analysis. The energy decomposition codes were taken from 
                                 ACS Nano 2020; 14(8): 9963-9971.

##  The code structure of OCTOPUS input files

    Below, we explain the steps involved in computing the weighted transition probability for Jellium-TMD calculation using the OCTOPUS package.

    inp_gs and inp_td are input files for the OCTOPUS calculation

    Files named 'info' generated in the ground state calculation and 'projections' obtained in the time-dependent calculations are required 
    for the post-processing.


    Prepare an input file 'My_tdden.inp' as shown in Jellium_TDDFT/Post_process_files/compute_WTP/To_compute_TDMAT/My_tdden.inp to compute 
    time-dependent density matrix. 
    
    Run tddenmat.py to compute the time-dependent density matrix. dmat.dat generated is used to compute the weighted transition probability. 


   Compute the weights of the system of interest using int_cube.py in Jellium_TDDFT/Post_process_files/compute_weights. The weights are 
   computed on the orbital density saved in the cube file format during the ground state calculations. 
   Jellium_TDDFT/Post_process_files/compute_weights/my_code.py can be employed to compute the weights using int_cube.py for a multiple number of states. 


   Once the weights of two regions in the cube file are computed, let's say region A and region B, weights.py in 
   Jellium_TDDFT/Post_process_files/compute_WTP/To_compute_WTP_using_TDMAT is used to compute the product of 
   weights of occupied states of region A and unoccupied states of region B.


   Then,Jellium_TDDFT/Post_process_files/compute_WTP/To_compute_WTP_using_TDMAT/weighted_prob.py is employed to 
   compute the product of the time-dependent density matrix with the product of weights. s_sum.py is used to compute
   the total sum of all transition probability from the occupied state of region A to the unoccupied state of region B. s_sum.py needs the total number of time steps as argument.
