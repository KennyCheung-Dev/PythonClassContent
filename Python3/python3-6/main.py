# Modifying DataFrames
# Merging DataFrames
# Plotting DataFrames & Styling

# Adding a brand new column
# Recall that DataFrames are similar to dict's
# in that the columns are the values in the dictionary
# We can add/delete columns using dict syntax

import numpy as np
import pandas as pd

# labels = ['a', 'b', 'c', 'd', 'e', 'f']
#
# d = {"item" : pd.Series(['apples', 'oranges', 'pears',
#                          'cherries', 'oears', 'coconuts'],
#                         index = labels),
#      "amount" : pd.Series([3, 1, 4, 1, 5, 9],
#                           index = labels)}
# df = pd.DataFrame(d)
# print(df)
#
# #Adding after the DataFrame has been built
# price = pd.Series([6, 8, 9, 4, 3, 299], index = labels)
# df["price"] = price
# print(df)
#
# # Operations between column
# df["Total Worth"] = df["price"] * df["amount"]
# print(df)
#
# # Delete columns:
# # del df["amount"]
# # deletedColumn = df.pop("price")
# # print(df)
# # print(deletedColumn)
#
# # Insert a column
# stolen = pd.Series([1, 1, 2, 1, 3, 5], index = labels)
# df.insert(4, "Stolen", stolen)
# print(df)
#
# # df.assign() a more powerful function for column insertion
# # Returns a new DataFrame (great for method chaining)
# # Can pass a function with one argument
# new_df = df.assign(Lost=df["Stolen"] * df["price"]).assign(Remain = lambda x : (df["Total Worth"] - x["Lost"]))
# print(new_df)
#
# # pd.concat() : concatenate given DataFrames together
# # along either axes
# # Does not look at labels/indices(if two DataFrames
# # share some labels/indices, they'll both get included
# pieces = [new_df["a":"c"], new_df["f":], new_df["d":"e"]]
# reordered = pd.concat([pieces[0], pieces[1], pieces[2]])
# print(reordered)
#
# # Append DataFrame onto DataFrame!
# # First create a dataframe of 1 entry "Turnips"
# turnipEntry = {
#     "item" : pd.Series({"f":"turnips"}),
#     "amount" : pd.Series({"f":82}),
#     "price" : pd.Series({"f":4}),
#     "Total Worth" : pd.Series({"f":328}),
#     "Stolen" : pd.Series({"f":38}),
#     "Lost" : pd.Series({"f":152}),
#     "Remain" : pd.Series({"f":176})
# }
#
# # Wrong Answer
# # turnipEntry = {# Wrong Answer
# #     "F": {# Wrong Answer
# #         "item":"turnips",# Wrong Answer
# #         "amount":82,# Wrong Answer
# #         "price":4,# Wrong Answer
# #         "Total Worth":328,# Wrong Answer
# #         "Stolen":38,# Wrong Answer
# #         "Lost":152,# Wrong Answer
# #         "Remain":176# Wrong Answer
# #     }# Wrong Answer
# # }# Wrong Answer
#
# turnipDF = pd.DataFrame(turnipEntry)
# appended_df = new_df.append(turnipDF)
# print(appended_df)
#
#
# # In-Class exercise:
# # Add a column with the total Remaining Amount on the amount
# df3 = appended_df.assign(RemainingAmount=appended_df["amount"] - appended_df["Stolen"])
# print(df3)

# Plotting a DataFrame!
import matplotlib.pyplot as plt
# plt.close("all")

# Prepare DataFrame
labels = ['apples', 'oranges', 'pears', 'cherries', 'peaches', 'coconuts']
day1 = pd.Series([3, 1, 4, 1, 5, 8], index=labels)
day2 = pd.Series([2, 7, 1, 8, 2, 8], index=labels)
day3 = pd.Series([2, 6, 5, 3, 5, 3], index=labels)
d = {"day1":day1, "day2":day2, "day3":day3}
df = pd.DataFrame(d)
print(df)

# Plot the DataFrame!
# plt.figure()
# df.plot()
# plt.show()



# Reversed axis
# df.T is what we want (Transposed)
# print(df.T)
# df.T.plot()
# plt.show()

# Can also apply dataFrame on different types of graphs
# df.plot(kind="bar")
# plt.show()

# Box Graph
# df.T.plot(kind="box")
# plt.show()

# hist Graph
# df.T.plot(kind="hist", subplots=True)
# plt.show()

# Pie Graph
# df.plot(kind="pie", subplots=True, figsize=[15, 6])
# plt.show()

# bar Graph
# df.T.plot.bar()
# plt.show()

# barH Graph
# df.T.plot.barh()
# plt.show()

# legend
# Stacked barH Graph
# df.T.plot.barh(stacked=True, legend=False)
# plt.show()

# layout: (x, y)
# Pie Graph
# df.plot(kind="pie", subplots=True, figsize=[15, 6], layout=(2, 2))
# plt.show()

# table: boolean
# barH Graph
df.T.plot.barh(table=True, figsize=[15, 7])
plt.show()


