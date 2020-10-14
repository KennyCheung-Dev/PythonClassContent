import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 1000)

# --------------------------------------------------------
# Read the data
g_data = pd.read_csv(r'g_data_revised.csv')
g_reviews = pd.read_csv(r'g_reviews_revised.csv')
a_data = pd.read_csv(r'a_data_revised.csv')
# --------------------------------------------------------

# Task1: Popularity vs Rating

# Scatter plot will be useful because both values are numeric

g_data_1 = g_data[['rating', 'installs']]
a_data_1 = a_data[['rating', 'rating_count']]

# g_data_1.plot.scatter()
# Params:
# x = x column
# y = y column
# s = scale of each point  how large
# c = color on each point

plt.close("all")


# Plot
g_data_1.plot.scatter(x="rating", y="installs", logy=True)


a_data_1.plot.scatter(x="rating", y="rating_count", logy=True, ylim=[1, 10000000])

# ---------------- ---------------- ---------------- ---------------- ----------------

# Task2 Popularity of apps in different categories

# We can :
# 1. Total number of downloads (skews heavily towards the categories with the most apps)
# 2. Number of apps
# 3. Number of popular apps (can define "popular apps" later)
# 4. Average number of downloads

# What should  we define app popularity with?
# top 5%

#  There are around 350 entries of apps on each app store, thats above 5%
# using the amount of installs/ratings

# Plan
# each plot is a bar plot, with the bars representing each categories
# height representing the number of popular apps

# Step1 : Count totals

# g_cat_counts = {}
# for cat in g_data["category"]:
#     if cat not in g_cat_counts:
#         g_cat_counts[cat] = 0
#     g_cat_counts[cat] += 1
# print(g_cat_counts)

# pandas offer a gorupby feature, can group by some functions like size, mean, sum
g_data_grouped = g_data.groupby(g_data["category"])
g_cat_totals = g_data_grouped.size()

a_data_grouped = a_data.groupby(a_data["category"])
a_cat_totals = a_data_grouped.size()

# print(a_data_totals)

g_pop_threshold = g_data.quantile(0.95, numeric_only=True)["installs"]
a_pop_threshold = a_data.quantile(0.95, numeric_only=True)["rating_count"]

# Count the popular!
g_cat_to_pop_count = {}
for cat, group in g_data_grouped:
    pop_count = 0
    for index, row in group.iterrows():
        if row['installs'] >= g_pop_threshold:
            pop_count += 1
    g_cat_to_pop_count[cat] = pop_count
# print(g_cat_to_pop_count)

a_cat_to_pop_count = {}
for cat, group in a_data_grouped:
    pop_count = 0
    for index, row in group.iterrows():
        if row['rating_count'] >= a_pop_threshold:
            pop_count += 1
    a_cat_to_pop_count[cat] = pop_count
# print(a_cat_to_pop_count)

# We have
# total count
# popular count
# threshold of popularity

g_data_2 = pd.DataFrame({"total": g_cat_totals, "popular": g_cat_to_pop_count})
a_data_2 = pd.DataFrame({"total": a_cat_totals, "popular": a_cat_to_pop_count})

_, g_ax = plt.subplots()
g_data_2.total.plot(kind="bar", ax=g_ax, color= "blue")
g_data_2.popular.plot(kind="bar", ax=g_ax, color= "red")

_, g_ax = plt.subplots()
a_data_2.total.plot(kind="bar", ax=g_ax, color= "blue")
a_data_2.popular.plot(kind="bar", ax=g_ax, color= "red")

# print(a_pop_threshold)

# ----------------------------------------------------

# Task3: Categories across platform
total_data_3 = pd.DataFrame({"google": g_cat_totals, "apple": a_cat_totals})
pop_data_3 = pd.DataFrame({"google": g_cat_to_pop_count, "apple": a_cat_to_pop_count})

# Plot!
total_data_3.plot.bar(figsize=[10, 5])
pop_data_3.plot.bar(figsize=[10, 5])

# ----------------------------------------------------------------------

#Homework :
#
# Data Wrangling
# Check all the content with .unique()  (get rid  of extra bits like "$")
# In that case, replace all not needed symbols, and use astype to change the data type
# Rename all the columns if they are problematic
# Remove all the columns that you don't need
# Remove all the entries that is empty in important values
# If you hae two datasets working together, unify their column names

# *********** Plot at least 2 easiest graph ***********


# ------------------------------------------------------------------------


# Task 4 -  Apps   across platforms
# Figure out what apps are on both platforms
# WE can simply go thorugh each app and check if its in the other side
# but its also slow and inefficient
# Dataframe.merge
# Params:
# right : The other dataframe
# on : string name of the column to merge on
# how: Type of joins, keep left or right? or inner (only matches) or outter
# suffixes:  [string, string], if there are other columns with the same  name, prefixes will be added
# default  would be '_a' '_r'

g_data =  g_data.drop_duplicates(subset="app_name", keep="first")
a_data =  a_data.drop_duplicates(subset="app_name", keep="first")

merged_data = g_data.merge(a_data, on="app_name", how='inner',  suffixes=['_g', '_a'])
print(merged_data.columns)


# Step2: Prepare DataFrames
merged_data_pop = merged_data[["app_name", "rating_count_g", 'rating_count_a']]
merged_data_rating = merged_data[["app_name", "rating_g", 'rating_a']]

# Step3: Plot!
merged_data_pop.plot.scatter(x="rating_count_g", y="rating_count_a", logx=True, logy=True)
merged_data_rating.plot.scatter(x="rating_g", y="rating_a")

# ---------- ---------- ---------- ---------- ---------- ---------- ----------

# Task5: Price of Popular Apps
# What a re the prices of the most popular paps on each  platform?
# Most of the apps are free, we will have to look at the paid ones
# We will mkae a  pie chart showing the  percentage of  free vs paid apps
# also look at their price vs popularity

#  Step1: Find all the paid apps
g_data_paid = g_data[g_data["price"] != 0]
a_data_paid = a_data[a_data["price"] != 0]

# Choose the elements that the top 5%
g_pop = g_data[g_data["installs"] > g_pop_threshold]
a_pop = a_data[a_data["rating_count"] > a_pop_threshold]

g_num_pop_paid = len(g_pop[g_pop["price"] != 0].index)
g_num_pop_free = len(g_pop.index) - g_num_pop_paid
a_num_pop_paid = len(a_pop[a_pop["price"] != 0].index)
a_num_pop_free = len(a_pop.index) - a_num_pop_paid

# Dataframe!
task_5_1 = pd.DataFrame({"paid":{"google":g_num_pop_paid, "apple":a_num_pop_paid},
                         "free":{"google":g_num_pop_free, "apple":a_num_pop_free}})
print(task_5_1)

# Step3: Prepare dataframes
g_data_paid = g_data_paid[["app_name", "price", "rating_count"]]
a_data_paid = a_data_paid[["app_name", "price", "rating_count"]]

# Plot!
task_5_1.T.plot.pie(subplots=True, figsize=[10, 5], legend=False)

# Plot!! Price vs popularityu
g_data_paid.plot.scatter(x="price", y="rating_count", logy=True, xlim=[0, 50], ylim=[1, 10000000])
a_data_paid.plot.scatter(x="price", y="rating_count", logy=True, xlim=[0, 50], ylim=[1, 10000000])

# ------------------------------------------------------------------------------------

# Show all the drawn graphs
plt.show()







