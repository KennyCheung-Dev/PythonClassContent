import pandas as pd
import matplotlib.pyplot as plt

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

_, g_ax = plt.subplots()
g_data_2.total.plot(kind="bar", ax=g_ax, color="blue")
g_data_2.popular.plot(kind="bar", ax=g_ax, color="red")

_, a_ax = plt.subplots()
a_data_2.total.plot(kind="bar", ax=a_ax, color="blue")
a_data_2.popular.plot(kind="bar", ax=a_ax, color="red")
plt.show()




