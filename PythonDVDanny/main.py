import pandas as pd
g_data = pd.read_csv(r'googleplaystore.csv')
a_data = pd.read_csv(r'AppleStore.csv')
g_reviews = pd.read_csv(r'googleplaystore_user_reviews.csv')

g_data = g_data[["App", "Category", "Rating", "Reviews", "Installs", "Type", "Price", "Last Updated"]]

# Drop data that does not have ratings
g_null_rating = g_data[g_data["Rating"].isnull()]
g_data = g_data.drop(g_null_rating.index)


# Drop the same entries from the review database
g_reviews = g_reviews[["App", "Translated_Review", "Sentiment"]]
for null_app in g_null_rating["App"]:
    g_reviews = g_reviews[g_reviews["App"] != null_app]


a_data = a_data[["track_name", "price", "rating_count_tot", "user_rating", "prime_genre"]]
a_null_rating = a_data[a_data["user_rating"].isnull()]
a_data = a_data.drop(a_null_rating.index)

#Unify column names
del g_data["Type"]
g_data.columns = ["app_name", "category", "rating", "rating_count", "installs", "price", "last_updated"]
a_data.columns = ["app_name", "price", "rating_count", "rating", "category"]



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

# print(g_data.describe())
# print(a_data.describe())

g_data["price"] = g_data["price"].str.replace("$", "")

g_data = g_data.astype({"price": "float64"})

g_data["installs"] = g_data["installs"].str.replace("+", "")
g_data["installs"] = g_data["installs"].str.replace(",", "")
g_data["installs"] = g_data["installs"].str.replace(" ", "")

g_data = g_data.astype({"installs": "int64"})

g_data = g_data.astype({"rating_count": "int64"})

g_data.to_csv('g_data.csv')
a_data.to_csv('a_data.csv')
g_reviews.to_csv('g_reviews.csv')


