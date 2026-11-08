# 1. Import liberaries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 2. Create dataset
data = {
    'Area': [1000, 1200, 1500, 1800, 2000],
    'Bedrooms': [2, 2, 3, 3, 4],
    'Price': [20, 25, 35, 40, 50]
}

# 3. Create DataFrame
HouseDF = pd.DataFrame(data)

# 4. Display first 5 rows
print(HouseDF.head())

#5. Dataset information
HouseDF.info()

# 6. Statistical summary
print(HouseDF.describe())

# 7. Column names
print(HouseDF.columns)

# 8. Pairplot
sns.pairplot(HouseDF)
plt.show()

# 9. Correlation heatmap
plt.figure(figsize=(8, 6))

sns.heatmap(
    HouseDF.corr(),
    annot = True,
    cmap = 'coolwarm'
)

plt.title('House Price Correlation')
plt.show()