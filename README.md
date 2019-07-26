# Data-Analysis-Workshop
Files for DISCNet school: session on Bayesian Parameter Inference and Model Comparison

The instructions for the exercises are in Eclipse1919-DISCNET.pdf   The other files are mostly MCMC chains, for students who wish to skip Project 1, or want to check results.    

HMC notes for DISCNET:  some extra notes on Hamiltonian Monte Carlo sampling.

Python (3.6) notebooks:
I've uploaded my python notebooks.  Note that they are not especially geared for teaching - they are my own rudimentary 
codes, but I hope that they are useful.

1. Eclipse 1919 Stan alpha      : does parameter inference, for alpha and nuisance parameters.  Also computes Evidence from Savage-Dickey density ratio
2. Eclipse 1919 Stan alpha prior: puts a strong (narrow) prior on alpha; effectively setting it to the Newtonian or Einstein value
3. MCE_Eclipse  : runs MCEvidence software on chains produced by (2)
4. GaussianMixtureModel_Eclipse   : fits one or more gaussians to the posterior from (1), and computes Bayes Factor analytically (if one gaussian fitted).

Alan Heavens and Harry Mootoovaloo
a.heavens@imperial.ac.uk
Imperial College
July 2019
