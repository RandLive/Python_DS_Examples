def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    # ECDF is short for empirical cumulative distribution function.
	
    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n

    return x, y
	

# Compute ECDF for versicolor data: x_vers, y_vers
x_vers, y_vers = ecdf(versicolor_petal_length)

# Generate plot
_ = plt.plot(x_vers, y_vers, marker='.', linestyle='none')

# Make the margins nice
plt.margins(0.02)

# Label the axes
_ = plt.xlabel('Versicolor petal length')
_ = plt.ylabel('ECDF')

# Display the plot
_ = plt.show()