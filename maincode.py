#1. Load Data

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_excel("Customer-Purchase-History.xlsx")
df.head()

#2. Sales Over Time
sales_trend = df.groupby('PurchaseDate')['TotalPrice'].sum()
plt.figure()
sales_trend.plot()
plt.title("Sales Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.show()

#3. Product Distribution
product_sales = df.groupby('Product')['TotalPrice'].sum()
plt.figure()
product_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title("Sales by Product")
plt.ylabel("")
plt.show()

#4. Product Category Analysis
category_sales = df.groupby('ProductCategory')['TotalPrice'].sum()
plt.figure()
category_sales.plot(kind='bar')
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.show()

#5. Payment Method Usage
payment = df['PaymentMethod'].value_counts()
plt.figure()
payment.plot(kind='bar')
plt.title("Payment Method Usage")
plt.xlabel("Method")
plt.ylabel("Count")
plt.show()

#6. Rating Distribution
plt.figure()
sns.histplot(df['ReviewRating'], bins=5)
plt.title("Customer Ratings")
plt.xlabel("Rating")
plt.show()

#7. Top 5 Products
top_products = df.groupby('Product')['TotalPrice'].sum().sort_values(ascending=False).head(10)
plt.figure()
top_products.plot(kind='bar')
plt.title("Top 5 Products")
plt.show()

#8. Monthly Sales Trend
df['Month'] = df['PurchaseDate'].dt.to_period('M')
monthly_sales = df.groupby('Month')['TotalPrice'].sum()
plt.figure()
monthly_sales.plot()
plt.title("Monthly Sales")
plt.show()

#9. Good vs Bad Feedback
df['Feedback'] = df['ReviewRating'].apply(lambda x: 'Good' if x >= 3 else 'Bad')
feedback = df['Feedback'].value_counts()
plt.figure()
feedback.plot(kind='pie', autopct='%1.1f%%')
plt.title("Customer Feedback")
plt.ylabel("")
plt.show()