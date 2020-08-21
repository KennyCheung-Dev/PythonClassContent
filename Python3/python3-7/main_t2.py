# Scenario:
# We are app developers looking to make a successful mobile app.
# We want to study the types of apps that are successful.

# We ll have to find  our own data, and create Data Visualization
# by using Pyhton and pandas

# Finding Data
# Kaggle is  the world's largest data science community

# Google Play Store Apps - Google Play Store
# AppStore - Apple App Store

# Planning on Our Projects?

# Task 1:
# Is there any correlation between popular apps and their ratings?
# Graph: Populartiy vs Rating

# Task2:
# What categories contain the most popular apps?
# Graph: Popularity in Categories

# Task3:
# Does one platform favour one category of apps over another
# WE  will create one combined plot that compares categories
# across the two datasets and see whether there  is  any
# difference between the platforms
# Graph: Categories across Platforms

# Task4:
# For apps that are on both platforms, how do the popularity/raintgs
# differ
# We will create two plots: one of popularity and one for
# ratings, that compare between the scores of each app on two
# different platforms

# Task5:
# Graph: Price of popular apps
# What are the price on the most popular apps on each platforms
# we will create a plot outlining the percentage of paid apps among
# the most popular apps,  as well as two plots (one for each dataset)
# comparing the price of paid apps and their popularity



# Final Project Preparation
# You'll be coming up with a plan for the project that is
# similar-sized to the example project
# Use Kaggle to look  at available datsets you are interested in
# Pick a topic, or we have some backup topics for you
# But we can't guarantee that they will be interesting to you.






# Data Wrangling

import pandas as pd

g_data = pd.read_csv(r'googleplaystore.csv')
a_data = pd.read_csv(r'AppleStore.csv')
print(g_data)
print(a_data)

# Homework:
# Find a domain you like,
# Find a dataset you might want to use for final





