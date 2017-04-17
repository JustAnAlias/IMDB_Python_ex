import numpy as np, matplotlib.pyplot as plt, pandas as pd,collections, sys, csv, urllib.request
from collections import OrderedDict
from operator import itemgetter
from tqdm import tqdm
df = pd.read_csv('movies.csv.csv', encoding='latin1').fillna(0)
#dataAP = dfA.as_matrix()

## A. 1 Histogram
#df1 = df.groupby(['rating', 'length', 'title'])
#df.plot(kind='bar', x='rating', y='length')
#df2 = df['title'].str.len()
#print(df2)
#df[['rating', 'length']][:10].plot(kind='bar')
#plt.xlabel('rating')
#plt.show()

#print("Question 2-----------------------")
#print("Create a graph showing both year and amount of movies made.")
df2 = df.groupby('year').count()['title']
#print(df2)

print(df['title'].str.len() < 250)
#dfp = df['title'].str.len() > 250
#sdfp = df[df.length > 250]
#print(dfp)

#print("Question 3-----------------------")
#print("Make a scatter-plot with year and length of movies. (Try to find clusters and explain them. Wild guesses are accepted).")
#df.plot(kind='scatter',x='year',y='length') # scatter plot
#plt.show()

#Create histograms of rating, length and length of title.
#
#Apply the MeanShift algorithm to identify all the clusters in the scatter-plot from Question 3.
#Create a median line for the scatter-plot made in Question 3.
#Make a scatter plot of: Length and year. Explain the connections between the different axis. (Optional:If the movie is animated or not)
