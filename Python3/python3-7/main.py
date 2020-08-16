# Final Project Outline
# Motivation for the project
# Finding good data
# Project Planning
# Important data into pandas
# Cleaning up data with pandas

# Final Project:
# Work with some rael-life data in order to come to a conclusion
# This will take us 2-3 weeks in total to finish
# Learn some new skills to use with pandas
# Prepare  for student  projects - in troduction at the end of the lesson
# Feel free to work along using the data provided!

# Description & Motivation
# Scenario:
# We are app  developers looking to make a successful mobile app.
# We want to study  the types of apps that are successful.

# How are we going to do that?
# With Data Visualization - Python and pandas!

# Goal:
# Through our analysis to determine the most popular
# types of apps, and look at the correlation between
# data  on # of installs, rating, and type
# We also want to look at the difference between Android users
# and iPhone users and see if they have different preferences
# At the end,  we want to come up with beautiful pandas visualizations
# that will help illustrate the data

# First step: Finding good data
# We want data that fits our goal and preferably has a high number of entries
# better analysis
# We will not collect our own data today (known as data scraping)
# Kaggle is a great place to find user-uploaded datasets
# Kaggle is the world's  largest data science community

# Our tutorial dataset:  Google Play Store Apps & Mobile App Store
# https://www.kaggle.com/lava18/google-play-store-apps/data#
# https://www.kaggle.com/ramamet4/app-store-apple-data-set-10k-apps
# Information on 10,000 apps scraped from the Google Play Store
# A bit older (2018) but this will do for our project today
# Contains 2 files: google play store.csv, and  googleplaystore_user_reviews.csv

# Google Play Store Apps
# https://www.kaggle.com/lava18/google-play-store-apps/data#
# Contains written reviews of each app
# Rows: represents a review of one of the apps in googleplaystore.csv
# Columns: App (name), Translated_Review (in English), Sentiment
# (Positive/Negative.Neutral), Sentiment_Polarity, Sentiment_Subjectivity

# Mobile App Store
# https://www.kaggle.com/ramamet4/app-store-apple-data-set-10k-apps
# Information on 7,200 apps scraped from the iOS App Store
# Similar age as our Google Play Store data, which means that it'll be a fair comparison
# Contains 2 files: appleStore.csv and appleStore_description.csv


#  We know  are datasets now, we can start planning for the different tasks
# we can udnertake as part of this project
# These tasks will all help us  come to some conclusion about the possible
# types of apps  we should create to maximize for success
# For each one of these tasks, we can create a separate DataFrame  and plot
# What do you want to learn from the datasets in order to achieve  our goal?

# Planning:
# Task 1: Popularity vs. Rating
# Is there any correlation between popular apps and their ratings?
# Does having a highly-rated app mean that it will be successful?

# We will create a single plot for this task that will plot each app's
# popularity and rating

# Task 2: Popularity of apps in different categories
# What categories contain t he most popular apps?
# Do the most popular apps come from only a few categories, or can apps
# of every category be successful?

# We will create two plots (one for each dataset) that will plot the number
# of popular apps of each category

# Task 3: Categories across platforms
# Does one platofrm favour one category of apps over another?
# We will create one combined plot  that compares categories  across the
# two datasets and see whether there is any difference between the platforms

# Task 4: Apps across platforms
# For apps that are on both platforms, how do the popularity/ratings differ?
# We will create two plots: one for popularity and one for ratings, that compare between
# the scores of each app on the two different platforms

# Task5: Price of popular apps
# What are the prices of the most popular apps on each platform?
# For the most popular paid apps, how much are people willing to pay
# for a good app?
# We will create a plot outlining the percentage of paid apps among the most popular apps,
# as well as two plots (one for each dataset)
# comparing the price of paid apps on their popularity

# Task 6: Update Time vs. Rating (Google Play Store only)
# Does the time of the most recent update affect the rating?
# We will create a time series plot that compares the last updated time and the
# average rating of the apps

# Now that we  know what we want to do with the data,
# we can get started on working on the project!
# Before we can d o any plotting though, we need to import the data into Python
# and pandas so we can actually work with it!
# Thankfully, pandas makes this very easy!

# Step1: download the data and save it to the directory
# Step2: Import pandas
# Step3: Use pandas' read_csv() function to import our data
# pandas.read_csv(): read a comma-separated values (csv) file into DataFrame
# YES! DATAFRAME RIGHT AWAY
# There are a lot of different parameters for this: We may end up
# using different ones for each of the plots, but for now let's just try
# doing it without using  any parameters!

import pandas as pd

g_data = pd.read_csv(r'googleplaystore.csv')
print(g_data.columns)
print(g_data["App"])

g_reviews = pd.read_csv(r'googleplaystore_user_reviews.csv')
a_data = pd.read_csv(r'AppleStore.csv')

# Our data are machine scraped, may contain apps that do not have data
# in certain columns that are essential to the project
# For now, we'll make  the decision that apps must have a rating score,
# and we'll also  forge some of the columns that are not necessary so we can save some memory
# We'll first keep working on the Google Play Store DataFrame
# What DataFrame operations do we use to do these tasks?

# Step1: Update our DataFrames to only include the columns we need
# App, Category, Rating, Reviews, Installs, Type, Price, Genres, Last Updated
# What DataFrame operations can we use to either delete the unnecessary
# columns, or create a new DataFrame containing the necessary columns?

# del g_data["Size"]
# del g_data["Content Rating"]
# del g_data["Genres"]
# del g_data["Current Ver"]
# del g_data["Android Ver"]

# OR

# Cleaning Up better
g_data = g_data[["App", "Category", "Rating", "Reviews", "Installs", "Type", "Price", "Last Updated"]]
print(g_data)

# Step 2: Finding the rows that do not have a ratings score
# The following is a useful notation for doing just that!
g_null_rating = g_data[g_data["Rating"].isnull()]
# print(g_data["Rating"].isnull())
print(g_null_rating.count())
# Thankfully, there's only 1474 rows that have a null  ratings,
# so we'll still have a lot of data to work with!

# Remove those 1474 rows!
g_data = g_data.drop(g_null_rating.index)
print(g_null_rating.index)

# Step4: Remove any reviews for these apps as well
# WE won't be using the individual reviews data much, j
# but let's practice selecting and dropping rows and columns with it
g_reviews = g_reviews[["App", "Translated_Review", "Sentiment"]]
# compare App Names in Null Rating list, and the review list
for null_app in g_null_rating["App"]:
    g_reviews = g_reviews[g_reviews["App"] != null_app]

# Clean up a_data
a_data = a_data[["track_name", "price", "rating_count_tot", "user_rating",
                 "prime_genre"]]
a_null_rating = a_data[a_data["user_rating"].isnull()]
a_data = a_data.drop(a_null_rating.index)
print(a_data)

# Making Important Decisions
# Since the t wo datasets come from different sources, the columns contained
# vary in name, and some may not exist
# For our project, let's decide on some common column names so we won't get confused
# app_name: the name of the app
# rating: the current rating that the app has
# rating_count: the number of ratings the app has
# category: the category/genre the app belongs in
# installs: number of installs (Android only)
# last_updated: date the app was last updated (Android only)

# Let's rename our columns in the two main DataFrames
del g_data["Type"]  # It's basically if its free or paid
print(g_data.columns)
g_data.columns = ["app_name", "category", "rating", "rating_count",
                  "installs", "price", "last_updated"]

# Let's rename our columns in the two main DataFrames
a_data.columns = ["app_name", "price", "rating_count", "rating", "category"]
# print(a_data)

# We don't have install numbers for iOS App Store apps, how do we
# determine  the popularity?
# We'll use rating_count to analyxe popularity-related tasks, as we can
# assume that more downloads will result in more ratings
# For Google Play Store apps, we'll analyze based on installs
# When analyzing both datasets together, we'll use
# rating_count for both to determine popularity

# So no need for installs :3 use rating count

#  More Important Decisions
# The categories don't match up between the datasets, how can we comapre them?
# To  solve this, we'll take  a look at the categories that are present,
# and make an informed decision on  what categories to assign to each.

# Step1: Find all the unique values in the "category" column
# for each dataset
# Hint: the pandas Series function .unique() will come in handy!
print(g_data["category"].unique())
print(a_data["category"].unique())

# Category that matches!
# Google Category	            Apple Category
# GAME	                        Games
# ART_AND_DESIGN, PRODUCTIVITY	Productivity
# WEATHER	                    Weather
# SHOPPING	                    Shopping
# COMICS, BOOKS_AND_REFERENCE	Reference, Book
# FINANCE	                    Finance
# TOOLS	                        Utilities
# EVENTS, TRAVEL_AND_LOCAL	    Travel
# SOCIAL, COMMUNICATION	        Social Networking
# SPORTS	                    Sports
# BUSINESS	                    Business
# BEAUTY, HEALTH_AND_FITNESS	Health & Fitness
# ENTERTAINMENT	                Entertainment, Music
# PHOTOGRAPHY, VIDEO_PLAYERS	Photo & Video
# MAPS_AND_NAVIGATION	        Navigation
# PARENTING, EDUCATION	        Education
# LIFESTYLE	                    Lifestyle
# FOOD_AND_DRINK	            Food & Drink
# NEWS_AND_MAGAZINES	        News
# MEDICAL	                    Medical

# Categories to be removed:
g_cat_to_remove  = ["AUTO_AND_VEHICLES", "HOUSE_AND_HOME",
                    "FAMILY", "DATING", "LIBRARIES_AND_DEMO",
                    "PERSONALIZATION", "1.9"]
for cat in g_cat_to_remove:
    g_data  = g_data[g_data["cateogrory"] != cat]
a_data = a_data[a_data["category"] != "Catalogs"] # Only one to remove from apple's side

# Step 4: Rename all categories... hard work
# Using a  dictionary, for look up
g_cat_dict = {"GAME": "Games", "ART_AND_DESIGN": "Productivity",
              "PRODUCTIVITY":"Productivity", "WEATHER": "Weather",
              "SHOPPING": "Shopping", "COMICS": "Books & Reference",
              "BOOKS_AND_REFERENCE": "Books & Reference", "FINANCE": "Finance",
              "TOOLS": "Utilities", "EVENTS": "Travel", "TRAVEL_AND_LOCAL": "Travel",
              "SOCIAL": "Social Networking", "COMMUNICATION": "Social Networking",
              "SPORTS": "Sports", "BUSINESS": "Business", "BEAUTY" : "Health & Fitness",
              "HEALTH_AND_FITNESS": "Health & Fitness", "ENTERTAINMENT" : "Entertainment",
              "PHOTOGRAPHY" : "Photo & Video", "VIDEO_PLAYERS": "Photo & Video",
              "MAPS_AND_NAVIGATION":"Navigation", "PARENTING": "Education",
              "EDUCATION": "Education", "LIFESTYLE": "Lifestyle",
              "FOOD_AND_DRINK": "Food & Drink", "NEWS_AND_MAGAZINES": "News",
              "MEDICAL": "Medical"}
g_data = g_data.replace(g_cat_dict)
a_cat_dict = {"Book": "Books & Reference", "Reference": "Books & Reference",
              "Music": "Entertainment"}
a_data = a_data.replace(a_cat_dict)

# Student Term Projects
# For the final section of this course, you'll be working on a large data visualization project
# of your own! Just like the one we are working through right  now!
# You should choose a topic that you are interested in researching in:
#  it could be related to demographics, economy, gaming
# Anything you want to learn more about through data and can find dat for!
# Use Kaggle and look at  their available datasets to help you choose  a topic if stuck
# Backup topics will be available if you cannot find one when we start working on the project,
# although  they are not guaranteed to be interesting to you!

# :3 Have Fun!

