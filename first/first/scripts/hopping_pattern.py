import numpy as np

# Generate hopping pattern
hopping_pattern = np.random.randint(0, 10, size=1000)

# Save hopping pattern to a file
np.savetxt('./hopping_pattern.txt', hopping_pattern, fmt='%d')
