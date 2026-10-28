# HYSPLIT Ensembles for the ARTofMELT 2023 Expedition

This repository contains code for post-processing of HYSPLIT ensembles that were run for the entire ARTofMELT 2023 expedition. The main post-processing that was performed was to apply a surface type mask to each individual coordinate along the trajectory path, attributing it to either land, ocean, sea-ice, or above the boundary layer. The python file py_funcs.py contains a collection of functions that were used to perform the masking, and the notebook masking.ipynb executes it. The requirements.txt file is a copy of the virtual environment that was used for running this code.

> ## Input data
> HYSPLIT ensembles were run locally using the pysplit python package. The ensembles were launched at 270m from the location of the Icebreaker Oden at every hour along its path. The meteorology was vertically and horizontally offset by ~250m to generate an ensemble of 27 trajectories. The input meteorological data was GDAS 1 degree resolution data. The version of HYSPLIT that was used was HYSPLIT v5.2.1.
> Sea-ice data was obtained via FTP from the University of Bremen and can be found by following the link: https://data.seaice.uni-bremen.de/amsr2/asi_daygrid_swath/n6250/

The masked trajectory data is available at the Bolin Centre Database with DOI:10.17043/matthew-2026-af7492-1. Please contact lead author Jessica Matthew at jessica.matthew@wadham.ox.ac.uk if you have any further questions.

### References

##### HYSPLIT can be found on the following websites:

Draxler, R.R. and Rolph, G.D., 2017. HYSPLIT (HYbrid Single-Particle Lagrangian Integrated Trajectory) Model access via NOAA ARL READY Website (http://www.ready.noaa.gov/HYSPLIT.php). NOAA Air Resources Laboratory, Silver Spring, MD.

Rolph, G., Stein, A., and Stunder, B., 2017. Real-time Environmental Applications and Display sYstem: READY. Environmental Modelling & Software, 95, 210-228, https://doi.org/10.1016/j.envsoft.2017.06.025.(http://www.sciencedirect.com/science/article/pii/S1364815217302360).

##### HYSPLIT development papers and references:
Stein, A.F., R.R. Draxler, G.D. Rolph, B.J.B. Stunder, M.D. Cohen, and F. Ngan , 2015. NOAA's HYSPLIT atmospheric transport and dispersion modelling system, Bulletin of the American Meteorological Society. [https://doi.org/ http://dx.doi.org/10.1175/BAMS-D-14-00110.1](https://doi.org/ http://dx.doi.org/10.1175/BAMS-D-14-00110.1)

Draxler, R.R. and G.D. Hess, 1998, An overview of the HYSPLIT_4 modelling system for trajectories, dispersion and deposition, Aust. Met. Mag., 47, 295-308.

Draxler, R.R. and G.D. Hess, 1997, Description of the HYSPLIT_4 modelling system, NOAA Technical Memorandum ERL ARL-224, December, 24 p.

##### University of Bremen Sea-Ice Data References:

Spreen, G., Kaleschke, L. and Heygster, G. (2008), Sea ice remote sensing using AMSR-E 89 GHz channels, J. Geophys. Res., 113, C02S03, https://doi.org/10.1029/2005JC003384.

University of Bremen AMSR2 ASI sea ice concentration v5.4, 6.25 km Arctic (Spreen et al., 2008), https://seaice.uni-bremen.de/sea-ice-concentration/ ; data from https://data.seaice.uni-bremen.de/amsr2/asi_daygrid_swath/n6250/ (accessed December 2023).


