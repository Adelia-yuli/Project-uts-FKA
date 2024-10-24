import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Set the title and subtitle
st.title("Fisika Komputasi Awan")
st.subheader("Adelia Yuli Santika 😎")

# Add a description
st.caption("Lingkaran dengan ukuran dan warna acak dan tersebar didalam lingkaran dengan radius 1")

# Create a button to generate new random data
if st.button('Data'):
    # Generate random data
    N = 100
    np.random.seed(42)
    r = np.random.rand(N)
    theta = np.random.rand(N) * 2 * np.pi
    size = np.random.rand(N) * 50
    color = np.random.rand(N)
    
    # Convert to cartesian coordinates
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    
    # Create scatter plot using Plotly Graph Objects
    fig = go.Figure()
    
    # Scatter plot for random points
    fig.add_trace(go.Scatter(
        x=x,
        y=y,
        mode='markers',
        marker=dict(
            size=size,
            color=color,
            opacity=0.6,
            colorscale='Viridis',
            line=dict(width=1, color='green')
        )
    ))

    # Add circular boundary (radius 1)
    fig.add_shape(
        type="circle",
        xref="x", yref="y",
        x0=-1, y0=-1, x1=1, y1=1,
        line=dict(color="red", width=1),
    )

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
    
    # Display the plot
    st.plotly_chart(fig)
