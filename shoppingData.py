#%%
# Import dependencies
import pandas as pd

# %%
file_path = "./Resources/shopping_data.csv"
df_shopping = pd.read_csv(file_path, encoding="ISO-8859-1")
df_shopping.head(5)

# %%
# Look at what data we have
df_shopping.columns
df_shopping.dtypes

# %%
#  Find null values
for column in df_shopping.columns:
    print(f"Column {column} has {df_shopping[column].isnull().sum()} null values")

# %%
# Drop null values
df_shopping = df_shopping.dropna()

# %%
# Find duplicate entries
print(f"Duplicate entries: {df_shopping.duplicated().sum()}")

# %%
# Remove the CustomerID Column
df_shopping.drop(columns=["CustomerID"], inplace=True)
df_shopping.head()

# %%
# Transform string column
def change_string(member):
    if member == "Yes":
        return 1
    else:
        return 0

df_shopping["Card Member"] = df_shopping["Card Member"].apply(change_string)
df_shopping.head()

# %%
# Transform annual income
df_shopping["Annual Income"] = df_shopping["Annual Income"] / 1000
df_shopping.head()

# %%
# Rename columns
df_shopping = df_shopping.rename(columns={"Card Member": "Card_Member", "Annual Income": "Annual_Income", "Spending Score (1-100)": "Spending_Score"})
df_shopping.head()

# %%
# Saving cleaned data
file_path = "./Resources/shopping_data_cleaned.csv"
df_shopping.to_csv(file_path, index=False)

# %%
