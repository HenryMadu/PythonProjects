import seaborn as sbs
import matplotlib.pyplot as pylt
import numpy as nup

data = nup.random.randint(1,19 ,size=(20,20)) # Generate a 10x10 array of random numbers from 1 to 15
sbs.heatmap(data, cmap='plasma') #  Create the heatmap
pylt.show() # Show the heatmap

#This code imports necessary libraries, generates a 20x20 array of random numbers, creates a heatmap from that data, and displays it.
# The heatmap will visually represent the random numbers, with colors indicating different values.