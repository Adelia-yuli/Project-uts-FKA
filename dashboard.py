import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Set the title and subtitle
st.title("Fisika Komputasi Awan")
st.subheader("Adelia Yuli Santika 😎")

# Add a description
st.caption("Data acak berubah setiap tombol ditekan")

# Function to generate random scatter data
def generate_data(N):
    r = np.random.rand(N)
    theta = np.random.rand(N) * 2 * np.pi
    size = np.random.rand(N) * 50
    color = np.random.rand(N)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y, size, color

# Initial plot
N = 100
x, y, size, color = generate_data(N)

# Create the figure
fig = go.Figure()

# Plot the scatter points
scatter = go.Scatter(
    x=x, y=y,
    mode='markers',
    marker=dict(
        size=size,
        color=color,
        opacity=0.6,
        colorscale='Viridis',
        line=dict(width=1, color='green')
    )
)
fig.add_trace(scatter)

# Plot the dashed lines from each point to the origin
for i in range(len(x)):
    fig.add_trace(go.Scatter(
        x=[0, x[i]], y=[0, y[i]],
        mode='lines',
        line=dict(color='green', width=1, dash='dash'),
        showlegend=False
    ))

# Draw concentric circles with radius intervals of 0.25
for r in np.arange(0.25, 1.1, 0.25):
    fig.add_shape(type="circle", xref="x", yref="y",
                  x0=-r, y0=-r, x1=r, y1=r,
                  line=dict(color="red", width=1, dash="dot"))

# Set axis properties to create a uniform circle
fig.update_xaxes(range=[-1.1, 1.1], zeroline=False)
fig.update_yaxes(range=[-1.1, 1.1], zeroline=False, scaleanchor="x", scaleratio=1)

# Set gridlines and layout properties
fig.update_layout(
    width=700,
    height=700,
    title="Data Acak yang berubah setiap tombol ditekan",
    xaxis_showgrid=True,
    yaxis_showgrid=True,
    showlegend=False,
)

# Display the initial plot
plot = st.plotly_chart(fig)

# Button to regenerate new random data
if st.button('Data'):
    x, y, size, color = generate_data(N)
    
    # Update scatter points
    fig.data[0].x = x
    fig.data[0].y = y
    fig.data[0].marker.size = size
    fig.data[0].marker.color = color

    # Update dashed lines
    for i in range(len(x)):
        fig.data[i + 1].x = [0, x[i]]
        fig.data[i + 1].y = [0, y[i]]

    # Update the plot
    plot.plotly_chart(fig)
