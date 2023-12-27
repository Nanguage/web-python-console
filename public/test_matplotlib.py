import matplotlib.pyplot as plt
import numpy as np

# Generate data
x = np.linspace(-2*np.pi, 2*np.pi, 1000)
y = np.linspace(-2*np.pi, 2*np.pi, 1000)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Create the plot
plt.figure(figsize=(10, 8))
plt.contourf(X, Y, Z, cmap='viridis')
plt.colorbar()

# Add titles and labels
plt.title("Cool Wave Pattern with Matplotlib", fontsize=18)
plt.xlabel("X-axis", fontsize=14)
plt.ylabel("Y-axis", fontsize=14)

# Show the plot
plt.show()
