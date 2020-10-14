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
g_reviews = pd.read_csv(r'googleplaystore_user_reviews.csv')

# Homework:
# Find a domain you like,
# Find a dataset you might want to use for final


# print(g_data["Genres"])
# print(g_data["Category"])

# Delete the not-needed columns
# del g_data["Size"]
# del g_data["Content Rating"]
# del g_data["Genres"]
# del g_data["Current Ver"]
# del g_data["Android Ver"]

# Select the used columns
g_data = g_data[["App","Category","Rating","Reviews","Installs","Price", "Last Updated"]]

# Find the rows that does not have a rating score
# and remove them from g_data
g_null_rating = g_data[g_data["Rating"].isnull()]
g_data = g_data.drop(g_null_rating.index)

# Remove any reviews for these apps as well!
g_reviews = g_reviews[["App", "Translated_Review", "Sentiment"]]

# Also remove the same entries from g_reviews
for null_app in g_null_rating["App"]:
    g_reviews = g_reviews[g_reviews["App"] != null_app]

# Clean up a_data

a_data = a_data[["track_name", "price", "rating_count_tot", "user_rating", "prime_genre"]]

a_null_rating = a_data[a_data["user_rating"].isnull()]
a_data = a_data.drop(a_null_rating.index)

# -------------------------------------------------------------------
# Rename the columns
g_data.columns = ["app_name", "category", "rating",
                  "rating_count", "installs", "price",
                  "last_updated"]
a_data.columns = ["app_name", "price", "rating_count",
                  "rating", "category"]

# print(g_data.columns)
# print(a_data.columns)



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
    g_data = g_data[g_data["category"] != cat]

a_data = a_data[a_data["category"] != "Catalogs"] # Only one to remove from apple's side

# Step 4: Rename all categories
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

# Get some basic statistics about our data
# print(g_data.describe())
# print(a_data.describe())





g_data["price"] = g_data["price"].str.replace("$", "")
g_data["installs"] = g_data["installs"].str.replace("+", "")
g_data["installs"] = g_data["installs"].str.replace(",", "")

g_data =  g_data.astype({"price" : "float64",
                         "rating_count" : "int64",
                         "installs" : "int64"})

# print(g_data["rating_count"].unique())
# print(g_data["installs"].unique())

# print(g_data.dtypes)
# print(a_data.dtypes)

print(g_data.describe())

g_data.to_csv('g_data_revised.csv')
a_data.to_csv('a_data_revised.csv')
g_reviews.to_csv('g_reviews_revised.csv')





# Clean Up Requirements:

# Check all the content with .unique()  (get rid  of extra bits like "$")
# Rename all  the columns if they are problematic
# Remove all the columns  that you don't need
# If you hae two datasets working together, unify their column names
#










