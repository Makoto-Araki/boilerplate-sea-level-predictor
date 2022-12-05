import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    # Get fig and ax
    fig, ax = plt.subplots(figsize=(12, 9))
    
    # Create scatter plot
    X1 = df['Year']
    Y1 = df['CSIRO Adjusted Sea Level']
    ax.scatter(X1, Y1)

    # Create first line of best fit
    X2 = df['Year']
    Y2 = df['CSIRO Adjusted Sea Level']
    result = linregress(X2, Y2)
    a = result.slope
    b = result.intercept
    data = pd.Series(np.arange(df['Year'].min(), 2051, 1))
    ax.plot(data, [a * t + b for t in data], color='red')

    # Create second line of best fit
    df_filtered = df[(df['Year'] >= 2000) & (df['Year'] <= df['Year'].max())]
    X3 = df_filtered['Year']
    Y3 = df_filtered['CSIRO Adjusted Sea Level']
    result = linregress(X3, Y3)
    a = result.slope
    b = result.intercept
    data = pd.Series(np.arange(df_filtered['Year'].min(), 2051, 1))
    ax.plot(data, [a * t + b for t in data], color='green')

    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_xlim(1850, 2100)
    ax.set_ylim(-2.0, 17.5)
    ax.set_xticks([1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0])
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()