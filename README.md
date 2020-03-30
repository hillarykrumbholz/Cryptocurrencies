# Cryptocurrencies

## Project Overview
To work with the K-means algorithm, the main unsupervised algorithm that groups similar data into clusters. Will build on this by speeding up the process using principal component analysis (PCA), which employs many different features.

## Resources
Data Sources: crypto_data.csv, principal_components.csv, X_cleaned_crypto <br>
Software: Jupyter Notebook, Python 3.7.6 <br>
Python dependencies: Pandas, hvPLot, PLotly, Scikit-learn

### Project Summary
To use unsupervised learning to analyze data on the cryptocurrencies traded on the market.  

A prominent investment bank, is interested in offering a new cryptocurrencies investment portfolio for its customers. The company needs a report of what cryptocurrencies are on the trading market and how cryptocurrencies could be grouped toward creating a classification for developing this new investment product.

### Project Objectives
- Prepare the data for dimensions reduction with PCA and clustering using K-means.
- Reduce data dimensions using PCA algorithms from sklearn.
- Predict clusters using cryptocurrencies data using the K-means algorithm form sklearn.
- Create some plots and data tables to present your results.
 
## Results
Code can be found [Here](https://github.com/hillarykrumbholz/Cryptocurrencies/blob/master/Challenge.ipynb)<br><br>

Elbow Curve<br>
![Elbow Curve](https://github.com/hillarykrumbholz/Cryptocurrencies/blob/master/Images/ElbowCurve.png)<br>

3D Scatter Plot<br>
![3D Scatter](https://github.com/hillarykrumbholz/Cryptocurrencies/blob/master/Images/3D_plot.png)<br>

Cluster Plot<br>
![Clusters](https://github.com/hillarykrumbholz/Cryptocurrencies/blob/master/Images/Scatter_plot.png)<br>

## Conclusion

After processing the data (removing null values, cryptocurrencies that aren't currently trading, and removing text features), I was left with 532 cryptocurrencies. The dimensions were then reduced to three principal components and an elbow curve was created to visualize and find the best value for K, which is 4. A 3D plot was then created to visualize the clusters based on the three principal components. Lastly, a scatter plot was created to display the clusters and their relation to the total of coins mined by their total supply. 
