import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 1000)

# -------------------------------------------------

# Read the csvs
g_data = pd.read_csv(r'g_data_revised.csv')
g_reviews = pd.read_csv(r'g_reviews_revised.csv')
a_data = pd.read_csv(r'a_data_revised.csv')

# -------------------------------------------------

# Task 1: Popularity vs Rating
# Scatter plot - will be useful if both values are numeric
# and when we are finding some trends

# Select the used columns
g_data_1 = g_data[['rating', 'installs']]
a_data_1 = a_data[['rating', 'rating_count']]

# DataFrame.plot.scatter
# Params:
# x = x column
# y = y columns
# s = scale on each point, how big they are
# c = color on each point

g_data_1.plot.scatter(x="rating", y="installs", logy=True)
a_data_1.plot.scatter(x="rating", y="rating_count", logy=True, ylim=[1, 10000000])

# -------------- --------------- --------------- --------------- --------------- ---------------

# Task2: Popularity of apps in different categories
# WE can do this in  a few different ways:
# 1. Total number of downloads (skews heavily towards the categories with the most apps)
# 2. Number of apps
# 3. Average number of downloads
# 4. Number of popular apps (top 5%)

# What we need:
# Total count of all apps in that category  *  DONE
# top 5% count in that category

# Step1 : Count total
# g_cat_counts = {}
# for cat in g_data["category"]:
#     if cat not in g_cat_counts:
#         g_cat_counts[cat] = 0
#     g_cat_counts[cat] += 1

# print(g_cat_counts)

# There is another way use group
g_data_grouped = g_data.groupby(g_data["category"])
g_cat_totals = g_data_grouped.size()
a_data_grouped = a_data.groupby(a_data["category"])
a_cat_totals = a_data_grouped.size()


# Finding the threshold for top 5%
g_pop_threshold = g_data.quantile(0.95, numeric_only=True)["installs"]
a_pop_threshold = a_data.quantile(0.95, numeric_only=True)["rating_count"]



# Actually counting the popular:
g_cat_to_pop_count = {}
for cat, group in g_data_grouped:
    pop_count = 0
    for index, row in group.iterrows():
        if row['installs'] >= g_pop_threshold:
            pop_count += 1
    g_cat_to_pop_count[cat] = pop_count

a_cat_to_pop_count = {}
for cat, group in a_data_grouped:
    pop_count = 0
    for index, row in group.iterrows():
        if row['rating_count'] >= a_pop_threshold:
            pop_count += 1
    a_cat_to_pop_count[cat] = pop_count

g_data_2 = pd.DataFrame({"total" : g_cat_totals, "popular":  g_cat_to_pop_count})
a_data_2 = pd.DataFrame({"total" : a_cat_totals, "popular":  a_cat_to_pop_count})

# Plot!
# plt.figure()
_, g_ax = plt.subplots()
g_data_2.total.plot(kind="bar", ax=g_ax, color="blue", logy=True)
g_data_2.popular.plot(kind="bar", ax=g_ax, color="red", logy=True)

_, g_ax = plt.subplots()
a_data_2.total.plot(kind="bar", ax=g_ax, color="blue", logy=True)
a_data_2.popular.plot(kind="bar", ax=g_ax, color="red", logy=True)

# ---------------------------------------------------------------------------------

# Categories across platform

# Build DataFrame
total_data_3 = pd.DataFrame({"google" : g_cat_totals, "apple": a_cat_totals})
pop_data_3 = pd.DataFrame({"google" : g_cat_to_pop_count, "apple": a_cat_to_pop_count})

# Plot!
total_data_3.plot.bar(figsize=[10, 5])
pop_data_3.plot.bar(figsize=[10, 5])

# ---------------------------------------------------------------------------

# Task4: Apps across platforms
# Steps  1: Figure out what apps are on both platforms
# We c an simply go through each a pp and check to see if it is in the other
# but its slow and inefficient

# DataFrame.merge
#params:
# right: The other dataframe to merge this dataframe with
# on: string name of the column to  merge on
# how: type of joins: if an item is not found  in another,
# keep left or right? or inner (only matches) or outer (keep all)
# suffixes: [string, string], these are gonna be added onto the entries names
# default = _l and _r , which means left and right
#  we will use _g and _a


g_data = g_data.drop_duplicates(subset="app_name", keep="first")
a_data = a_data.drop_duplicates(subset="app_name", keep="first")
merged_data = g_data.merge(a_data, on="app_name", how="inner", suffixes=['_g', '_a'])
# print(merged_data)

# Step2: Prepare Dataframes
merged_data_pop = merged_data[["app_name", "rating_count_g", "rating_count_a"]]
merged_data_rating = merged_data[["app_name", "rating_g", "rating_a"]]

# Plot!
merged_data_pop.plot.scatter(x="rating_count_g", y="rating_count_a", logx=True, logy=True)
merged_data_rating.plot.scatter(x="rating_g", y="rating_a")

# ------------------------------------------------------------------------------------------

#Task5: Price of Popuplar Apps
# What are the prices of the most popular apps on each platforms?


# Step1: Find all the paid apps
# Method 1:   For loop    too slow
g_data_paid = g_data[g_data["price"] != 0]
a_data_paid = a_data[a_data["price"] != 0]
# print(g_data_paid.size)

# Chooses the elements that are in the the top  5%
g_pop = g_data[g_data['installs'] > g_pop_threshold]
a_pop = a_data[a_data['rating_count'] > a_pop_threshold]

#Count of popular and free
g_num_pop_paid = len(g_pop[g_pop["price"] != 0].index)
g_num_pop_free = len(g_pop.index) - g_num_pop_paid
a_num_pop_paid = len(a_pop[a_pop["price"] != 0].index)
a_num_pop_free = len(a_pop.index) - a_num_pop_paid

# DataFrames
task_5_1 = pd.DataFrame({"paid":{"google":g_num_pop_paid, "apple":a_num_pop_paid},
                         "free":{"google":g_num_pop_free, "apple":a_num_pop_free}})

task_5_1.sum().plot.pie(figsize=[5,5], legend=False)

task_5_1.T.plot.pie(subplots=True, figsize=[10, 5], legend=False)


# Plot
g_data_paid.plot.scatter(x="price", y="rating_count", logy=True, xlim=[0, 50], ylim=[1, 10000000])
a_data_paid.plot.scatter(x="price", y="rating_count", logy=True, xlim=[0, 50], ylim=[1, 10000000])

# ------------------------------------------------------------------------------------------

newDateTime = pd.to_datetime(g_data["last_updated"])
newDataTimeSeries = pd.Series(newDateTime)
del g_data["last_updated"]
g_data["last_updated"] = newDataTimeSeries

newDateTime2 = pd.to_datetime(g_pop["last_updated"])
newDataTimeSeries2 = pd.Series(newDateTime)
del g_pop["last_updated"]
g_pop["last_updated"] = newDataTimeSeries2


g_data_6 = g_data.resample('2Q', on="last_updated").agg({"rating": np.mean})
print(g_data_6)

g_data_6.plot.bar(ylim=[3.0, 5.0])

g_pop_6 = g_pop.resample('2Q', on="last_updated").count()[["app_name"]].rename(columns={"app_name": "count"})
g_pop_6.plot.bar()

# show plots
plt.show()


######## During the break please also look at your database and
######## Think of any questions you have for me6