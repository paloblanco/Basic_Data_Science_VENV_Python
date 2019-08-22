#%%
import csv
import sqlite3
import pandas as pd
import math
# Use svg backend for better quality
import matplotlib
matplotlib.use("svg")
import matplotlib.pyplot as plt

%matplotlib inline
plt.style.use('ggplot')
matplotlib.rcParams['figure.figsize'] = (10.0, 5.0) # you should adjust this to fit your screen

# Rocco is trying to learn altair better
import altair as alt

#%%
