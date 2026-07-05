print("Sales Dashboard Project Started Successfully") 

import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Load dataset
df = pd.read_csv(
    r"C:\Users\admin\Documents\Sales_Data_Visualization_Project\Dataset\sales_data.csv"
)

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Display column names
print("COLUMN NAMES:")
print(df.columns.tolist())

# Convert Order Date column into datetime format
df['Order Date'] = pd.to_datetime(
    df['Order Date'],
    dayfirst=True,
    errors='coerce'
)

print("\nDATE COLUMN CONVERTED SUCCESSFULLY")

# -----------------------------------
# DATA CLEANING
# -----------------------------------

# Check missing values
print("\nMISSING VALUES BEFORE CLEANING:")
print(df.isnull().sum())

# Remove missing values
df = df.dropna()

print("\nMISSING VALUES AFTER CLEANING:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

print("\nDUPLICATE ROWS REMOVED")

# -----------------------------------
# DATA TRANSFORMATION
# -----------------------------------

# Create Month column
df['Month'] = df['Order Date'].dt.month_name()

# Create Year column
df['Year'] = df['Order Date'].dt.year

# Create Day column
df['Day'] = df['Order Date'].dt.day

print("\nNEW COLUMNS CREATED SUCCESSFULLY")

# -----------------------------------
# DISPLAY UPDATED DATA
# -----------------------------------

print("\nFIRST 5 ROWS OF CLEANED DATA:")
print(df.head())

print("\nDATA TYPES:")
print(df.dtypes)

print("\nFINAL DATASET SHAPE:")
print(df.shape)

print("\n========== KPI ANALYSIS ==========")

# Total Sales
total_sales = df['Sales'].sum()

print("\nTOTAL SALES:")
print(round(total_sales, 2))

# Total Profit
if 'Profit' in df.columns:

    total_profit = df['Profit'].sum()

    print("\nTOTAL PROFIT:")
    print(round(total_profit, 2))

else:
    print("\nPROFIT COLUMN NOT AVAILABLE")

# Total Orders
if 'Order ID' in df.columns:

    total_orders = df['Order ID'].nunique()

    print("\nTOTAL ORDERS:")
    print(total_orders)

# Total Quantity
if 'Quantity' in df.columns:

    total_quantity = df['Quantity'].sum()

    print("\nTOTAL QUANTITY SOLD:")
    print(total_quantity)
    
df.to_csv(
    r"C:\Users\admin\Documents\Sales_Data_Visualization_Project\Dataset\sales_data.csv",
    index=False
)

print("\nCLEANED DATASET SAVED SUCCESSFULLY!")    
# -----------------------------------
# MONTHLY SALES TREND CHART
# -----------------------------------

monthly_sales = df.groupby('Month')['Sales'].sum()

plt.figure(figsize=(10, 5))

monthly_sales.plot(kind='line', marker='o')

plt.title("Monthly Sales Trend")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.grid(True)

plt.savefig("monthly_sales_trend.png")
plt.show()

# -----------------------------------
# REGION-WISE SALES CHART
# -----------------------------------

region_sales = df.groupby('Region')['Sales'].sum()

plt.figure(figsize=(8, 5))

region_sales.plot(kind='bar')

plt.title("Sales by Region")

plt.xlabel("Region")

plt.ylabel("Sales")

plt.savefig("monthly_sales_trend.png")
plt.show()

# -----------------------------------
# CATEGORY-WISE SALES PIE CHART
# -----------------------------------

category_sales = df.groupby('Category')['Sales'].sum()

plt.figure(figsize=(7, 7))

plt.pie(
    category_sales,
    labels=category_sales.index,
    autopct='%1.1f%%'
)

plt.title("Sales by Category")

plt.savefig("monthly_sales_trend.png")
plt.show()

# -----------------------------------
# TOP 10 PRODUCTS CHART
# -----------------------------------

top_products = df.groupby('Product Name')['Sales'].sum().sort_values(
    ascending=False
).head(10)

plt.figure(figsize=(12, 6))

top_products.plot(kind='bar')

plt.title("Top 10 Selling Products")

plt.xlabel("Product Name")

plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.savefig("monthly_sales_trend.png")
plt.show()

# -----------------------------------
# INTERACTIVE REGION-WISE SALES CHART
# -----------------------------------

# Group data
region_category_sales = (
    df.groupby(['Region', 'Category'])['Sales']
      .sum()
      .reset_index()
)

# Plot Interactive Chart
interactive_chart = px.bar(
    region_category_sales,
    x='Region',
    y='Sales',
    color='Category',
    barmode='group',
    text_auto=True,
    title='Interactive Region-wise Sales'
)

interactive_chart.show()

# Business Insights
print("\n========== BUSINESS INSIGHTS ==========")

region_sales = df.groupby('Region')['Sales'].sum()
category_sales = df.groupby('Category')['Sales'].sum()
top_products = df.groupby('Product Name')['Sales'].sum()

print(f"Highest Sales Region : {region_sales.idxmax()}")
print(f"Best Category        : {category_sales.idxmax()}")
print(f"Top Selling Product  : {top_products.idxmax()}")
print(f"Average Sales        : {df['Sales'].mean():.2f}")