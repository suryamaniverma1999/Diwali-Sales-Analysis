import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("../data/Diwali_Sales_Data.csv")

# Display basic info
print(df.info())

# Data Cleaning
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# Sales Analysis by Gender
plt.figure(figsize=(6, 4))
sns.countplot(x='Gender', data=df, palette='pastel')
plt.title("Sales by Gender")
plt.savefig("../images/sales_by_gender.png")

# Show summary statistics
print(df.describe())

# Save the cleaned dataset
df.to_csv("../data/Diwali_Sales_Cleaned.csv", index=False)

