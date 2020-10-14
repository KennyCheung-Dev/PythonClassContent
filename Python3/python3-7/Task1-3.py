# Use these lines to export into csv
# g_data.to_csv('g_data_revised.csv')
# a_data.to_csv('a_data_revised.csv')
# g_reviews.to_csv('g_reviews_revised.csv')

# ----------------------------------------------------------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', 500)
pd.set_option("display.max_rows", 1000)

# ----------------------------------------------------------------

# Read CSVs
g_data =  pd.read_csv(r'g_data_revised.csv')
a_data =  pd.read_csv(r'a_data_revised.csv')
g_reviews =  pd.read_csv(r'g_reviews_revised.csv')

# ----------------------------------------------------------------

# Task1: Popularity vs Rating

# Scatter plot will be useful because both values are numeric
# We can see eah app on t he plot and see where they are
# located in terms  of  popularity vs quality

g_data_1 = g_data[['rating', 'installs']]
a_data_1 = a_data[['rating', 'rating_count']]

# DataFrame.plot.scatter

# Determine the parameters to give
# x = x column
# y = y column
# s = scale on each opint, how large
# c = color on each point

# Plot!

# plt.close("all")
# plt.figure()

# g_data_1.plot.scatter(x="rating", y="installs")

# seems like a lot of the data is clustered at the bottom
# can't see clearlty
# a trick is to use log-scaling plot
# ticks.spaces on axis to have larger space when more values exists

g_data_1.plot.scatter(x="rating", y="installs", logy=True)
a_data_1.plot.scatter(x="rating", y="rating_count", logy=True, ylim=[1, 10000000])


# ----------------------------------------------------------------

# Task2 Popularity of apps in different categories
# We can do this in a few different ways:
# 1. Total number of downloads (skews heavily towards the categories with the most apps)
# 2. Number of apps
# 3. Number of popular apps (can  define "popular apps" later)
# 4. Average number of downloads(doesn't work when there are a lot of apps
#    that may be relatively unknown in a single category)
# Number 3 is a bit more complicated but seems the most well-rounded

# How should we define app populairty?
# We can use the top % of  apps overall
# But what %?

# Top 5 % of apps seems like a good number
# it  is about 350 for each of the app stores, and the amount of installs/ratings
# these apps have are at the very high end of the datasets we have

# Plan we'll make two plots for each of the datasts
# Each plot is a bar plot, with the bars  representing each categories
# height representing the number  of popular apps

# WE NEED Total count and Popular 5% count,  two set of data

# We don't have a specific column for this, we'll have to count it ourselves

# Step1: Count totals
# g_cat_counts = {}
# for cat in g_data["category"]:
#     if cat not in g_cat_counts:
#         g_cat_counts[cat] = 0
#     g_cat_counts[cat] +=  1
# print(g_cat_counts)

# There is another way to do this.
# pandas provide a groupby feature, we  can group by some  functions like size, mean, sum
g_data_grouped = g_data.groupby(g_data["category"])
g_cat_totals = g_data_grouped.size()
# print(g_cat_totals)

# Let's do the same with a_data
a_data_grouped = a_data.groupby(g_data["category"])
a_cat_totals = a_data_grouped.size()
# print(a_cat_totals)

# Now let's try to go for the top 5%
# df.quantile return the values for each column at a given percentile
# so if we use '0.95' as the parameter, we will get the threshold value
# separating  the bottom 95% and the top 5%
# we'll  store the popularity threshold to use later

# print(g_data.quantile(0.95, numeric_only = True))
# print(a_data.quantile(0.95, numeric_only = True))

g_pop_threshold = g_data.quantile(0.95, numeric_only = True)['installs']
a_pop_threshold = a_data.quantile(0.95, numeric_only = True)['rating_count']

# Count the pouplar!
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

# Making DataFrame
g_data_2 = pd.DataFrame({"total": g_cat_totals, "popular": g_cat_to_pop_count})
a_data_2 = pd.DataFrame({"total": a_cat_totals, "popular": a_cat_to_pop_count})

# Plot!
_, g_ax = plt.subplots()
g_data_2.total.plot(kind="bar", ax=g_ax, color="blue")
g_data_2.popular.plot(kind="bar", ax=g_ax, color="red")

# Plot!
_, g_ax = plt.subplots()
a_data_2.total.plot(kind="bar", ax=g_ax, color="blue")
a_data_2.popular.plot(kind="bar", ax=g_ax, color="red")

# Pie Chart
g_data_2.plot.pie(subplots=True, figsize=[15, 6], legend=False)
a_data_2.plot.pie(subplots=True, figsize=[15, 6], legend=False)

# --------------------------------------------------------------------------------

#Task3 : Categories across platform
total_data_3 = pd.DataFrame({"google": g_cat_totals, "apple": a_cat_totals})
pop_data_3 = pd.DataFrame({"google": g_cat_to_pop_count, "apple": a_cat_to_pop_count})

# Plot!
total_data_3.plot.bar(figsize=[10, 5])

pop_data_3.plot.bar(figsize=[10, 5])



# --------------------------------------------------------------------------------

# Task4: Apps across platforms
# Figure out what apps are on both platforms
# We can simply go through each app and check to see if it is in the other
# but it is slow and inefficient
# We can use DataFrame.merge
# we can merge by either index or a specified  column
# Params:
# right: The other dataframe to merge this dataframe with
# on: string name of the column to merge on
# how: type of join, if an item is not found in another, keep left or right? or inner(only matches) or outer
# suffixes: [string, string], if there  are other columns with the same name,
# assign specified suffix to each column from each DataFrame

# what params do we want to use?
# on : this should be the column we want to base on "app_name"
# how: since we only want to keep apps that are on both, we will  use "inner"
# suffixe: the dfault suffixes used are '_l' and '_r' left and right
# but we want to use '_g' and '_a'

# merged_data = g_data.merge(a_data, on="app_name", how="inner", suffixes=['_g', '_a'])
# print(merged_data)
# We have duplicates!

# We can use brtueforce  again, but slow
# DataFrame.drop_duplicates()
# Params:
# subset: columns we want to consider (default is all columns, only removes full duplicate rows)
# keep: "first", "last", or False  to drop all duplicates

g_data = g_data.drop_duplicates(subset="app_name", keep="first")
a_data = a_data.drop_duplicates(subset="app_name", keep="first")
merged_data = g_data.merge(a_data, on="app_name", how="inner", suffixes=['_g', '_a'])
# print(merged_data)

# Step2: Prepare DataFrames
merged_data_pop = merged_data[["app_name", "rating_count_g", "rating_count_a"]]
merged_data_rating = merged_data[["app_name", "rating_g", "rating_a"]]

# Plot!
merged_data_pop.plot.scatter(x="rating_count_g", y="rating_count_a", logx=True, logy=True)

# Plot!
merged_data_rating.plot.scatter(x="rating_g", y="rating_a")

#  -----------------------------------------------------------------------------

# Task5: Price of Popular Apps
# What are the prices of the most popular apps on each platform?
# Most of the apps are free,  but we do have some paid ones to look at
# We wil make a pie char4t showing the percentage of free vs paid apps
# also look at their price vs popularity

# Step1: Find all the paid apps
# Method 1 for loop, but slow
# Or we can use df.loc !
g_data_paid = g_data[g_data["price"] != 0]
a_data_paid = a_data[a_data["price"] != 0]

# Chooses the elements that are the top 5%
g_pop = g_data[g_data["installs"] > g_pop_threshold] #google's pop threshold is full score of 5
a_pop = a_data[a_data["rating_count"] > a_pop_threshold]

g_num_pop_paid = len(g_pop[g_pop["price"] != 0].index)
g_num_pop_free = len(g_pop.index) - g_num_pop_paid
a_num_pop_paid = len(a_pop[a_pop["price"] != 0].index)
a_num_pop_free = len(a_pop.index) - a_num_pop_paid

# DataFrame!
task_5_1 = pd.DataFrame({"paid": {"google": g_num_pop_paid, "apple":a_num_pop_paid},
                         "free": {"google": g_num_pop_free, "apple":a_num_pop_free}})
print(task_5_1)

# Step3: Prepare dataframes
g_data_paid = g_data_paid[["app_name", "price", "rating_count"]]
a_data_paid = a_data_paid[["app_name", "price", "rating_count"]]

#Plot!
task_5_1.T.plot.pie(subplots=True, figsize=[10, 5], legend=False)

# We want a price of popular apps on both platform
# Combine the two!
task_5_1.sum().plot.pie(figsize=[5, 5], legend=False)

# Plot!  Price vs popularity
g_data_paid.plot.scatter(x="price", y="rating_count", logy=True, xlim=[0, 50], ylim=[1, 10000000])
a_data_paid.plot.scatter(x="price", y="rating_count", logy=True, xlim=[0, 50], ylim=[1, 10000000])


# -----------------------------------------------------------------.,

# If the app hasn't been updated for a while, does that affect the rating?
# b = pd.to_datetime(g_data["last_updated"])
# g_data["last_updated"] = b
# Before : January 7, 2018   After: 2018-01-07   a  format that pd can work with

# Resample allow us to group time into period length
# 2Q means two-quater, which means half year
# g_data_6 = g_data.resample('2Q', on='last_updated').agg({"rating":np.mean})


# Show all plots
plt.show()