## Plasmon Induced Charge Transfer Dynamics in Metallic Nanoparticle-MoSe2 Nanoﬂake Heterostructures
The project contains all the input files related to the work.

### The code structure

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

