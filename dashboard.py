import streamlit as st
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Set the title and subtitle
st.title("Fisika Komputasi Awan")
st.subheader("Adelia Yuli Santika 😎")

# Create a circle patch
circle = Circle((0, 0), 1, color='red', fill=False, linewidth=2, linestyle='-', alpha=0.2)

# Initialize lists for storing data points
x = [0]
y = [0]
color = [(0.0, 0.7, 0.0)]
size = [371]

# Button to generate new random data
if st.button("Data"):
    for _ in range(111):
        x0 = 2 * (random.random() - 0.5)  # Random x between -1 and 1
        y0 = 2 * (random.random() - 0.5)  # Random y between -1 and 1
        
        # Ensure points are within the unit circle
        if x0**2 + y0**2 > 1:
            # Adjust y0 to lie on the circle's edge
            y0 = np.sqrt(1 - x0**2) if y0 > 0 else -np.sqrt(1 - x0**2)

        # Append the new point data
        x.append(x0)
        y.append(y0)
        color.append((random.random(), random.random(), random.random()))  # Random RGB color
        size.append(3713 * random.random())  # Random size for the scatter points

# Create the plot
fig, ax = plt.subplots(figsize=(16, 16))  # Adjusted size for better display
ax.add_patch(circle)

# Draw dashed lines from origin to points
for i in range(1, len(x)):
    ax.plot([0, x[i]], [0, y[i]], color='blue', linestyle='--', alpha=0.3)

# Scatter plot of random points
scatter = ax.scatter(x, y, c=color, s=size, alpha=0.4)

# Set labels and properties
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title('Data Acak yang Berubah Setiap Tombol Ditekan')
ax.grid(True, linestyle='-.')
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.tick_params(axis='both', labelsize=12)

# Display the plot in Streamlit
st.pyplot(fig)
st.caption("Lingkaran dengan ukuran dan warna acak dan tersebar di dalam lingkaran dengan radius 1")
st.divider()
