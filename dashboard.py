import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import random
import math

# Set the title and subtitle
st.title("Fisika Komputasi Awan")
st.subheader("Adelia Yuli Santika 😎")
# Button to regenerate new random data for points (but circles stay the same)
if st.button('Data'):
    x, y, size, colors = generate_data(N)  # Generate new points data
    fig = plot_figure(x, y, size, colors)  # Plot with new data
    st.pyplot(fig)

# Function to generate random scatter data
def generate_data(N):
    r = [random.uniform(0, 1) for _ in range(N)]  # Random radial distances
    theta = [random.uniform(0, 2 * math.pi) for _ in range(N)]  # Random angles
    size = [random.uniform(10, 50) for _ in range(N)]  # Random sizes
    colors = ['#%06X' % random.randint(0, 0xFFFFFF) for _ in range(N)]  # Random colors
    x = [r[i] * math.cos(theta[i]) for i in range(N)]  # Convert to x coordinates
    y = [r[i] * math.sin(theta[i]) for i in range(N)]  # Convert to y coordinates
    return x, y, size, colors

# Function to plot the fixed circles, scatter points, and dashed lines
def plot_figure(x, y, size, colors):
    fig, ax = plt.subplots(figsize=(6, 6))

    # Plot the concentric circles (remain unchanged)
    for radius in [0.25, 0.5, 0.75, 1.0]:
        circ = Circle((0, 0), radius, color='red', fill=False, linestyle='--', linewidth=1)
        ax.add_patch(circ)

    # Plot dashed lines connecting points to origin
    for i in range(len(x)):
        ax.plot([0, x[i]], [0, y[i]], linestyle='--', color='green', linewidth=0.5)

    # Plot random scatter points
    ax.scatter(x, y, s=size, c=colors, alpha=0.6, edgecolors="green", linewidth=1)

    # Set axis limits and properties
    ax.set_xlim([-1.1, 1.1])
    ax.set_ylim([-1.1, 1.1])
    ax.set_aspect('equal')
    ax.set_xticks([-1, -0.5, 0, 0.5, 1])
    ax.set_yticks([-1, -0.5, 0, 0.5, 1])
    ax.grid(True)

    return fig

# Initial plot
N = 100  # Number of points
x, y, size, colors = generate_data(N)  # Generate initial data

# Add a description
st.caption("Lingkaran dengan ukuran dan warna acak dan tersebar didalam lingkaran dengan radius 1")

# Create and display the initial figure (with fixed circles)
fig = plot_figure(x, y, size, colors)
st.pyplot(fig)
