#%%
# Initial imports
import pandas as pd
from sklearn.cluster import KMeans
#from matplotlib import pyplot as plt
import plotly.express as px
import hvplot.pandas

# %%
# Load data
file_path = "./Resources/shopping_data_cleaned.csv"
df_shopping = pd.read_csv(file_path)
df_shopping.head(10)

#%%
df_shopping.dtypes

# %%
# See what the points look like 
df_shopping.plot.scatter(x="Annual_Income", y="Spending_Score")

# %%
# Function to cluster and plot dataset
def test_cluster_amount(df_shopping, clusters):
    model = KMeans(n_clusters=clusters, random_state=5)

    # Fitting the model
    model.fit(df_shopping)

    # Add a new class column to the df
    df_shopping["class"] = model.labels_

# %%
# Test with 2 clusters
test_cluster_amount(df_shopping, 2)
df_shopping.hvplot.scatter(x="Annual_Income", y="Spending_Score", by="class")

# %%
