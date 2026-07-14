# ================= Import Libraries ==================
import pandas as pd
import matplotlib.pyplot as plt

# ================== Load Dataset ======================
df = pd.read_csv("D:/Python Project/Zamato Data Analysis/Data/Zomato_sample_data.csv")

# ================ Data Inspection =====================

#Checking the data
print(df.head())

#How many no of rows and columns are in the data?
print("\nNo of rows and columns in the data: ",df.shape)

#What are the column names
print("\nColumn names of the dataset:\n ", df.columns)

#Check if there is any missing value:
print("\nCheck for Missing values:\n", df.isnull().sum())

#Define Statistical summary
print("\nStatistical Summary: \n", df.describe())

#Get Information about every column
print("\nInformation about every Column:\n")
df.info()

#Checking for unique value
print("\nChecking Unique Values for the following Column:\n")
print("Online_Order:", df["online_order"].unique())
print("Book Table: ",df["book_table"].unique())
print("Listed In: ", df["listed_in(type)"].unique())

# ================= Data Cleaning ======================

#Convert Rate column into float and remove "/5"
df["rate"] = df["rate"].str.replace("/5", "", regex=False)
df["rate"] = df["rate"].astype(float)

# ============= Feature Engineering ====================
def cost_category(cost):
    if cost < 300:
        return "Budget"
    elif 300 <= cost <= 700:
        return "Moderate"
    else:
        return "Expensive"

df["Cost_Category"] = df["approx_cost(for two people)"].apply(cost_category)
print("\nCategorized Cost into Cost Category\n")
print(df[["approx_cost(for two people)", "Cost_Category"]].head(10))

# ============ Exploratory Data Analysis ===============

# ================= Restaurant Type ====================

#1 -> Which restaurant type is the most common?
restaurant_type = df["listed_in(type)"].value_counts()
print("\nNumber of Restaurant based on their Type: \n",restaurant_type )

restaurant_type.plot(kind="bar", figsize=(8,5))

plt.title("Number of Restaurants by Type")
plt.xlabel("Restaurant Type")
plt.ylabel("Count")

plt.tight_layout()
plt.savefig("D:/Python Project/Zamato Data Analysis/Images/01_common_restaurant_type.png", dpi=300)
plt.show()
plt.close()

#2 -> Which restaurant type has the highest average rating? 
restaurant_rating = df.groupby("listed_in(type)")['rate'].mean()
print("\nAverage Rating of different type of Restaurant: \n",restaurant_rating)

restaurant_rating.plot(kind = "bar", figsize=(8,5))

plt.title("Restaurant with the Average Rating")
plt.xlabel("Restaurant Type")
plt.ylabel("Average Rating")

plt.tight_layout()
plt.savefig("D:/Python Project/Zamato Data Analysis/Images/02_average_rating_by_restaurant_type.png", dpi=300)
plt.show()
plt.close()

#3 -> Which restaurant type receives the highest total votes? 
restaurant_type_rating = df.groupby("listed_in(type)")['votes'].sum().sort_values(ascending=False)
print("\nRestaurant Type with the hightest Votes: \n",restaurant_type_rating)

restaurant_type_rating.plot(kind = "bar", figsize=(8,5))

plt.title("Restaurant with the highest votes")
plt.xlabel("Type of Restaurant")
plt.ylabel("Votes")

plt.tight_layout()
plt.savefig("D:/Python Project/Zamato Data Analysis/Images/03_total_votes_by_restaurant_type.png", dpi=300)
plt.show()
plt.close()

#4 -> Which restaurant type has the highest average cost?
restaurant_cost = df.groupby("listed_in(type)")["approx_cost(for two people)"].mean().sort_values(ascending=False)
print("\nApprox Cost for Two based on the Retaurant Type: \n",restaurant_cost )

restaurant_cost.plot(kind="bar", figsize=(8,5))

plt.title("Average Cost by Restaurant Type")
plt.xlabel("Restaurant Type")
plt.ylabel("Average Cost")

plt.tight_layout()
plt.savefig("D:/Python Project/Zamato Data Analysis/Images/04_average_cost_by_restaurant_type.png", dpi=300)
plt.show()
plt.close()

# ================= Online Order =======================

#5 -> Do restaurants offering online ordering receive more customer engagement?
online_votes = df.groupby("online_order")["votes"].mean()
print("\nNumber of votes for Restaurants offering Online Ordering Service: \n",online_votes)

online_votes.plot(kind="bar", figsize=(8,5))

plt.title("Average Votes by Online Order")
plt.xlabel("Online Order")
plt.ylabel("Average Votes")

plt.tight_layout()
plt.savefig("D:/Python Project/Zamato Data Analysis/Images/05_online_order_vs_votes.png", dpi=300)
plt.show()
plt.close()

#6 -> Do restaurants with online ordering charge more?
online_restaurant_cost = df.groupby("online_order")["approx_cost(for two people)"].mean()
print("\nApprox Cost of Restaurants offering Online Ordering Service: \n",online_restaurant_cost )

online_restaurant_cost.plot(kind="bar", figsize=(8,5))

plt.title("Average Cost by Online Ordering Restaurants")
plt.xlabel("Online Ordering Restaurants")
plt.ylabel("Average Cost")

plt.tight_layout()
plt.savefig("D:/Python Project/Zamato Data Analysis/Images/06_average_cost_by_online_order.png", dpi=300)
plt.show()
plt.close()

# =================== Table Booking ====================

#7 -> Does table booking affect ratings?
table_rating  = df.groupby("book_table")["rate"].mean()
print("\nAverage Rate of Restaurants offering Table Booking Service: \n",table_rating )

table_rating.plot(kind="bar", figsize=(8,5))

plt.title("Average Rating by Table Booking")
plt.xlabel("Table Booking")
plt.ylabel("Average Rating")

plt.tight_layout()
plt.savefig("D:/Python Project/Zamato Data Analysis/Images/07_table_booking_vs_rating.png", dpi=300)
plt.show()
plt.close()

# ================= Ratings & Cost ====================

#8-> How are restaurant ratings distributed? 
plt.figure(figsize=(8,5))
plt.hist(df["rate"], bins=10)

plt.title("Distribution of Restaurant Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Restaurants")

plt.tight_layout()
plt.savefig("D:/Python Project/Zamato Data Analysis/Images/08_distribution_of_rating.png", dpi=300)
plt.show()
plt.close()

#9-> How are restaurant cost distributed? 
plt.figure(figsize=(8,5))
plt.hist(df["approx_cost(for two people)"], bins=10)

plt.title("Distribution of Restaurant Cost")
plt.xlabel("Approximate Cost for Two")
plt.ylabel("Number of Restaurants")

plt.tight_layout()
plt.savefig("D:/Python Project/Zamato Data Analysis/Images/09_distribution_of_cost.png", dpi=300)
plt.show()
plt.close()

#10 -> Does spending more result in better restaurant ratings?
plt.figure(figsize=(8,5))
plt.scatter(df["approx_cost(for two people)"], df["rate"])

plt.title("Cost vs Rating")
plt.xlabel("Approximate Cost for Two")
plt.ylabel("Restaurant Rating")

plt.tight_layout()
plt.savefig("D:/Python Project/Zamato Data Analysis/Images/10_cost_vs_rating.png", dpi=300)
plt.show()
plt.close()

correlation = df["approx_cost(for two people)"].corr(df["rate"])
print(f"\nCorrelation between Cost and Rating: {correlation:.2f}")

#11 -> Which cost category has the highest average rating?
cost_category_rating = df.pivot_table(
    values="rate",
    index="Cost_Category",
    aggfunc="mean"
)
print("\nAverage Rating based on Cost Category: \n",cost_category_rating)

cost_category_rating.plot(kind="bar", figsize=(8,5))

plt.title("Average Rating by Cost Category")
plt.xlabel("Cost Category")
plt.ylabel("Average Rating")

plt.tight_layout()
plt.savefig("D:/Python Project/Zamato Data Analysis/Images/11_average_rating_by_cost_category.png", dpi=300)
plt.show()
plt.close()

# ============= Final Business Summary Report =============

#Restaurant Type Summary 
restaurant_summary = df.groupby("listed_in(type)").agg(
    Average_Rating=("rate", "mean"),
    Lowest_Rating=("rate", "min"),
    Average_Cost=("approx_cost(for two people)", "mean"),
    Average_Votes=("votes", "mean"),
    Highest_Votes=("votes", "max")
)
restaurant_summary = restaurant_summary.sort_values(      
    by="Average_Rating",
    ascending=False
)
restaurant_summary = restaurant_summary.round(2)
print("\nSummary of different Restaurant Type: \n",restaurant_summary)

#Online Order Summary
online_order_summary = df.groupby("online_order").agg(
    Lowest_Votes=("votes", "min"),
    Highest_Votes=("votes", "max"),
    Average_Rating=("rate", "mean"),
    Average_Cost=("approx_cost(for two people)", "mean")    
    )
online_order_summary = online_order_summary.sort_values(      
    by="Average_Rating",
    ascending=False
)
online_order_summary = online_order_summary.round(2)
print("\nSummary of Restaurant offering Online Ordering Service: \n",online_order_summary)