# Working with some real=life data in order to come to a conclusion
# This will take us 3 - 4 weeks in total

# Scenario:
# We are app developers looking to make a successful mobile app.
# We want to study the types of app that are successful

# Wtih Data Visualization - Python and pandas

# Through our analysism, we would want to  determine
# the most popuplar types of apps,
# Looking at # of installs,  ratings types and such
# Would also want to look at the difference between Android and iPhone

# Finding good data
# Kaggle is the world's largest data sciene community

# Planning
# What do we want to learn from the datasets
# in order to achieve our goal?




# Final Project:
# For the final section
# You'll be working on a large data visualization project of
# your own!
# You should choose a topic that you are interested
# It could be related to anything, demographics, economy, gaming
# Use Kaggle to look at the available datasets
# BE SURE TO FIND ONE THAT DOESN't NEED TOO MUCH DATA WRANGLING
# We have some backup topics, if you cannot  find one,
# but we can't guarantee that you'll be interested in them

# For this week, homework:
# Find a database/dataset you are interested in
# analyzing
# Any topic
# The more entries, the more accurate your analyzes would be


#------------------------------------------------------------------------------------------------------------

# Task1: Popularity v.s. Rating
# Is there any correlation between popular apps and their ratings?
# Deos having a highly-rated app mean that it'll be more successful?
# Create a single plot fro this task.

# Task2: Popularity of apps in different  categories
# What categories apps would be the most popular?
# two plots, one for each dataset

# Task3: Categories across platforms
# Does one  platform favour one category of apps over another?
# We will create one combined plot comparing categories across  the two
# datasets

# Task4: Apps across platforms
# For apps that are on both platforms, how do the popularity/ratings differ?
# Two plots, one for popularity and one  for ratings.

# Task5: Price of popular apps
# What are the prices of the most popular apps on each platform?
# For  the most popular  paid apps, how much are people  willing to pay
# 1 plot outlining the percentage of paid apps among the most popular apps
# maybe  2 more (one for each dataset) comparing  the price of paid apps
# and  their popularity

# Task6: Update time vs. Rating (Google play store only)
# Does the time of the most recent update affect the rating?
# a times series plot that compares the last updated time
# and the average rating of the apps

# Import Data into Pandas

import pandas as pd
g_data = pd.read_csv(r'googleplaystore.csv')
g_reviews = pd.read_csv(r'googleplaystore_user_reviews.csv')

a_data = pd.read_csv(r'AppleStore.csv')
# a_description = pd.read_csv(r'appleStore_description.csv')

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# print(g_data.columns)

del g_data["Size"]
del g_data["Content Rating"]
del g_data["Genres"]
del g_data["Current Ver"]
del g_data["Android Ver"]
del g_data["Type"]

# print(g_data.columns)

# print(g_data["Rating"])
g_null_rating = g_data[g_data["Rating"].isnull()]
g_data = g_data.drop(g_null_rating.index)
# print(g_data["Rating"])

# Remove  reviews null fields in the g_reviews database
# print(g_reviews.columns)
g_reviews = g_reviews[["App", "Translated_Review", "Sentiment"]]
for null_app in g_null_rating["App"]:
    g_reviews = g_reviews[g_reviews["App"] != null_app]

a_data = a_data[["track_name", "price", "rating_count_tot", "user_rating", "prime_genre"]]
a_null_rating = a_data[a_data["user_rating"].isnull()]
a_data = a_data.drop(a_null_rating.index)

# print(g_data.columns)
# print(a_data.columns)

# Rename the columns
g_data.columns = ["app_name", "category", "rating",
                  "rating_count", "installs", "price",
                  "last_updated"]
a_data.columns = ["app_name", "price", "rating_count",
                  "rating", "category"]


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
    g_data  = g_data[g_data["category"] != cat]
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

# print(g_data["category"].unique())
# print(a_data["category"].unique())

# print(g_data.describe())
# print(a_data.describe())

# Replace strings by: Series.str.replace()
g_data["price"] = g_data["price"].str.replace("$", "")
g_data["installs"] = g_data["installs"].str.replace("+", "")
g_data["installs"] = g_data["installs"].str.replace(",", "")

# Still object?
# Have to actually transfer the data types
# using df.astype()
g_data = g_data.astype({"price": "float64"})

# print(g_data.dtypes)
# print(g_data["price"].unique())

# print(g_data.describe())

# Homework:
# Convert the datatype for "rating_count" and "installs"

g_data = g_data.astype({"rating_count": "int64"})
g_data = g_data.astype({"installs": "int64"})

# print(g_data.dtypes)
# print(a_data.dtypes)


# ----------------------------------------------------------------------

# Graphing!
# First, export the data
g_data.to_csv('g_data_revised.csv')
g_reviews.to_csv('g_reviews_revised.csv')
a_data.to_csv('a_data_revised.csv')

