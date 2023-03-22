#Use the data to complete the following tasks:

Use Pandas to import the data from epa-sea-level.csv.
Use matplotlib to create a scatter plot using the Year column as the x-axis and the CSIRO Adjusted Sea Level column as the y-axis.
Use the linregress function from scipy.stats to get the slope and y-intercept of the line of best fit. Plot the line of best fit over the top of the scatter plot. 
Make the line go through the year 2050 to predict the sea level rise in 2050.
Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset. 
Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000.
The x label should be Year, the y label should be Sea Level (inches), and the title should be Rise in Sea Level.

Code:
from grpc import intercept_channel
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig = plt.figure()
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'],s=8)

    # Create first line of best fit
    res1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x1 = np.arange(df['Year'].min(),2051,1)
    y1 = res1.intercept + res1.slope*x1
    plt.plot(x1,y1)

    # Create second line of best fit
    df2 = df[df['Year']>=2000]
    res2 = linregress(df2['Year'], df2['CSIRO Adjusted Sea Level'])
    x2 = np.arange(df2['Year'].min(),2051,1)
    y2 = res2.intercept + res2.slope*x2
    plt.plot(x2,y2)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
  
