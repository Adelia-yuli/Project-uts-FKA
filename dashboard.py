import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd

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
    size = np.random.rand(N) * 30
    color = np.random.rand(N)
    
    # Convert to cartesian coordinates
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    # Create DataFrame
    df = pd.DataFrame({'x': x, 'y': y, 'size': size, 'color': color})
    
    # Create scatter plot using Plotly
    fig = px.scatter(df, x='x', y='y', size='size', color='color', 
                     title="Data Acak yang berubah setiap tombol ditekan",
                     width=700, height=700)

    # Add circular boundary
    fig.update_layout(
        shapes=[
            dict(type="circle",
                 xref="x", yref="y",
                 x0=-1, y0=-1, x1=1, y1=1,
                 line_color="red")
        ],
        xaxis_range=[-1.1, 1.1], yaxis_range=[-1.1, 1.1]
    )
    
    # Display the plot
    st.plotly_chart(fig)
