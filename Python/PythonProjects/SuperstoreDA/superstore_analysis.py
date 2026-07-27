# ===========================================================
# SAMPLE SUPERSTORE SALES ANALYSIS
# Beginner Data Analysis Project
# Dataset: Sample - Superstore.csv
# ===========================================================

import pandas as pd

# Display all rows and columns in terminal
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)

print("="*70)
print("SAMPLE SUPERSTORE SALES ANALYSIS")
print("="*70)

# ---------------- LOAD DATASET ----------------
df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")

# ---------------- DATASET EXPLORATION ----------------
print("\nFirst 5 Rows")
print(df.head())

print("\nLast 5 Rows")
print(df.tail())

print("\nShape:", df.shape)

print("\nColumns")
print(df.columns.tolist())

print("\nData Types")
print(df.dtypes)

print("\nDataset Information")
df.info()

print("\nStatistical Summary")
print(df.describe(include="all"))

print("\nMemory Usage")
print(df.memory_usage())

print("\nUnique Values")
print(df.nunique())

# ---------------- DATA CLEANING ----------------
print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

df = df.drop_duplicates()

df["Order Date"] = pd.to_datetime(df["Order Date"], format="mixed")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], format="mixed")

print("\nDataset cleaned successfully!")

# ---------------- BASIC ANALYSIS ----------------
print("\nTotal Orders:", len(df))
print("Total Sales:", round(df["Sales"].sum(),2))
print("Total Profit:", round(df["Profit"].sum(),2))
print("Average Sales:", round(df["Sales"].mean(),2))
print("Average Profit:", round(df["Profit"].mean(),2))
print("Highest Sale:", round(df["Sales"].max(),2))
print("Lowest Sale:", round(df["Sales"].min(),2))
print("Total Quantity:", df["Quantity"].sum())

groups = [
    "Category","Sub-Category","Region","State",
    "City","Segment","Ship Mode"
]

for g in groups:
    print("\n===== {} ANALYSIS =====".format(g.upper()))
    print(df.groupby(g)[["Sales","Profit"]].sum().sort_values("Sales", ascending=False))

print("\nDiscount Analysis")
print(df.groupby("Discount")[["Sales","Profit"]].mean())

print("\nMonthly Sales")
print(df.groupby(df["Order Date"].dt.month_name())["Sales"].sum())

print("\nYearly Sales")
print(df.groupby(df["Order Date"].dt.year)["Sales"].sum())

print("\nTop 10 Products")
print(df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10))

print("\nTop 10 Customers")
print(df.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False).head(10))

print("\nTop 10 States")
print(df.groupby("State")["Sales"].sum().sort_values(ascending=False).head(10))

print("\nBusiness Insights")
print("Best Category:", df.groupby("Category")["Sales"].sum().idxmax())
print("Best Region:", df.groupby("Region")["Sales"].sum().idxmax())
print("Best State:", df.groupby("State")["Sales"].sum().idxmax())
print("Top Customer:", df.groupby("Customer Name")["Sales"].sum().idxmax())
print("Most Used Ship Mode:", df["Ship Mode"].mode()[0])

print("\nProject Completed Successfully!")