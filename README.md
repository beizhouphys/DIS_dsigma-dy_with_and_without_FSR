# DIS_dsigma-dy_with_and_without_FSR
 
Here you can download the data files for the CCDIS dσdy without and with FSR (final state radiation).
 
The folder "**without_FSR**" has those without FSR, i.e., QCD-based DIS calculations. The calculations go to next-to-next leading order (NNLO) in QCD, in comparison to previous NLO calculations. The calculations are detailed in the paper https://arxiv.org/abs/2303.13607, led by Dr. Keping Xie (https://inspirehep.net/authors/1618109). 
If you look at Fig.17 of the paper on page 28, you can see that the difference between CTEQ18 (NNLO) and previous NLO calculations can be as large as 10% around 10 TeV and 20% around 1 EeV, which is mainly due to NNLO vs NLO. If you use these data, please **cite** https://arxiv.org/abs/2303.13607, thanks.
 
The folder "**with_FSR**" is the above plus final state radiation, based on https://arxiv.org/abs/2403.07984.
There are two subfolders. "numu_numubar/" is for numu/numubar CCDIS, and "nutau_nutaubar/" is for nutau/nutaubar CCDIS. Because the FSR correction depends on the charged lepton mass, the FSR corrections depend on neutrino flavors. If you use these data, please **cite** both https://arxiv.org/abs/2403.07984. and https://arxiv.org/abs/2303.13607, thanks.
 
All the results are for neutrino scattering with an **isoscalar target** (i.e., proton/2+neutron/2). 
The file names have the information of the parent neutrino energies (e.g., Enu1E+02GeV), and information of neutrino (i.e. _neu) or antineutrino (i.e. _ant).
In the files, the **1st column** are the y values. The **2nd columns** are the dσdy values.
 
Also in the folder is an example Python code for reading the files and making a figure.
  
If you have any questions, please contact me at beizhousuper@gmail.com. 
 
Later I'll upload the **NCDIS** dsigma/dy.
