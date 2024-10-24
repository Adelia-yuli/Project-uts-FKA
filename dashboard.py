import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd

# Set the title
st.title("Fisika Komputasi Awan")
st.subheader("Adelia Yuli Santika 😎")

# Create a button
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
    
    # Plotly scatter plot
    fig = px.scatter(df, x='x', y='y', size='size', color='color', 
                     title="Data Acak yang berubah setiap tombol ditekan",
                     width=700, height=700)
    
    # Display the plot
    st.plotly_chart(fig)
