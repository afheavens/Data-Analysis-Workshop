star_number = np.array([11, 5, 4, 3, 6, 10, 2])
n           = len(star_number)
x           = np.array([-1.261, -0.160, 0.334, 0.348, 0.587, 0.860, 1.079]).reshape(n,1)
y           = np.array([-0.160, -1.107, 0.472, 0.360, 1.099, 1.321, -0.328]).reshape(n,1)
Ex          = np.array([-0.587, -0.557, -0.186, -0.222, 0.080, 0.158, 1.540]).reshape(n,1)/19.8

# Here I have used Dx_plate_II 
# You can choose other plates 
# Or increase the number of data points by combining data from different plates 
Dx_plate_II = np.array([-1.416, -1.221, -1.054, -1.079, -1.012, -0.999, -0.733]).reshape(n,1) + 1.50    
sigma       = np.array([0.05])
