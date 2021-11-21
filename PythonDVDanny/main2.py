import pandas as pd
import matplotlib.pyplot as plt


pd.set_option('display.max_columns', None)
pd.set_option("max_rows", None)

g_data = pd.read_csv(r'g_data.csv')
a_data = pd.read_csv(r'a_data.csv')
g_reviews = pd.read_csv(r'g_reviews.csv')


g_data_1 = g_data[['rating', 'installs']]
a_data_1 = a_data[['rating', 'rating_count']]

plt.close("all")

# g_data_1.plot.scatter(x="rating", y="installs", logy=True)
#
# a_data_1.plot.scatter(x="rating", y="rating_count", logy=True)

# plt.show()

#--------------------------------------------------------------

g_data_grouped = g_data.groupby(g_data["category"])
g_cat_total = g_data_grouped.size()

a_data_grouped = a_data.groupby(a_data["category"])
a_cat_total = a_data_grouped.size()

g_pop_thres = g_data.quantile(0.95, numeric_only=True)["installs"]
a_pop_thres = a_data.quantile(0.95, numeric_only=True)["rating_count"]

g_cat_to_pop_count = {}
for cat, group in g_data_grouped:
    pop_count = 0
    for index, row in group.iterrows():
        if row['installs'] >= g_pop_thres:
            pop_count += 1
    g_cat_to_pop_count[cat] = pop_count

a_cat_to_pop_count = {}
for cat, group in a_data_grouped:
    pop_count = 0
    for index, row in group.iterrows():
        if row['rating_count'] >= a_pop_thres:
            pop_count += 1
    a_cat_to_pop_count[cat] = pop_count

g_data_2 = pd.DataFrame({"total" : g_cat_total, "popular" : g_cat_to_pop_count})
a_data_2 = pd.DataFrame({"total" : a_cat_total, "popular" : a_cat_to_pop_count})

# Bar Charts
# _, g_ax = plt.subplots()
# g_data_2.total.plot(kind="bar", ax=g_ax, color="blue")
# g_data_2.popular.plot(kind="bar", ax=g_ax, color="red")
#
# _, a_ax = plt.subplots()
# a_data_2.total.plot(kind="bar", ax=a_ax, color="blue")
# a_data_2.popular.plot(kind="bar", ax=a_ax, color="red")
#
# #Pie Charts
# g_data_2.plot.pie(subplots=True, figsize=[15, 7], legend=False)
# a_data_2.plot.pie(subplots=True, figsize=[15, 7], legend=False)

#Task 3 : Categories across Platforms
# total_data_3 = pd.DataFrame({"google" : g_cat_total, "apple" : a_cat_total})
# pop_data_3 = pd.DataFrame({"google" : g_cat_to_pop_count, "apple" : a_cat_to_pop_count})
#
# total_data_3.plot.bar(figsize=[8, 3])
# pop_data_3.plot.bar(figsize=[8, 3])

# Task 4: Apps across Platforms
g_data = g_data.drop_duplicates(subset="app_name", keep="first")
a_data = a_data.drop_duplicates(subset="app_name", keep="first")
#
# merged_data = g_data.merge(a_data, on="app_name", how="inner", suffixes=["_g", "_a"])
#
# merged_data_pop = merged_data[["app_name", "rating_count_g", "rating_count_a"]]
# merged_data_rating = merged_data[["app_name", "rating_g", "rating_a"]]
#
# merged_data_pop.plot.scatter(x="rating_count_g", y="rating_count_a", logx=True, logy=True)
# merged_data_rating.plot.scatter(x="rating_g", y="rating_a", logx=True, logy=True)

#Task 5
g_data_paid = g_data[g_data["price"] != 0]
a_data_paid = a_data[a_data["price"] != 0]

g_pop = g_data[g_data["installs"] > g_pop_thres]
a_pop = a_data[a_data["rating_count"] > a_pop_thres]

#Number of paid apps in g - Choose the apps with price != 0
#Number of free apps in g

g_num_pop_paid = len(g_pop[g_pop["price"] != 0].index)
g_num_pop_free = len(g_pop.index) - g_num_pop_paid
a_num_pop_paid = len(a_pop[a_pop["price"] != 0].index)
a_num_pop_free = len(a_pop.index) - a_num_pop_paid

#DataFrame!
task_5_1 = pd.DataFrame({"paid" : {"google": g_num_pop_paid, "apple": a_num_pop_paid},
                         "free" : {"google": g_num_pop_free, "apple": a_num_pop_free}
                         })

g_data_paid = g_data_paid[["app_name", "price", "rating_count"]]
a_data_paid = a_data_paid[["app_name", "price", "rating_count"]]

task_5_1.T.plot.pie(subplots=True, figsize=[10, 5], legend=False)


plt.show()







# import time
# start_time = time.time()
#
# li1 = ["Hi"] * 800000000
#
# li2 = ["Wow"] * 800000000
#
# print("--- %s seconds ---" % (time.time() - start_time))