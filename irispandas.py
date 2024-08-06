import pandas as pd
import numpy as np

iris = pd.read_csv("iris.csv")
print(iris)
df = pd.read_csv('iris.csv')# Load the dataset
# Display the first 10 rows
print("First 10 rows of the dataset:")
print(df.head(10))

print("*" * 50)

#2
df = pd.DataFrame(iris)
# Calculate summary statistics for each feature
summary_stats = df.describe()
print(summary_stats)

print("*" * 50)

#3
# Calculate the mean sepal length for each species
mean_sepal_length_by_species = df.groupby('Species')['Sepal.Length'].mean().reset_index()
mean_sepal_length_by_species.columns = ['Species', 'mean_sepal_length']

# Merge the mean values back into the original DataFrame
df = df.merge(mean_sepal_length_by_species, on='Species', how='left')

print(df.groupby('Species')['Sepal.Length'].mean().reset_index(name='mean_sepal_length'))

# Display the DataFrame with the new columns
print(df.head())

print("*" * 50)

#4
# Check for missing values
print("Missing values in each column before imputation:")
print(df.isnull().sum())

# Identify numeric columns
numeric_columns = df.select_dtypes(include='number').columns

# Replace missing values in numeric columns with the mean of each column
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())

# Verify that there are no missing values left
print("\nMissing values in each column after imputation:")
print(df.isnull().sum())

print("*" * 50)

#3.Check for missing values

print("Missing values in each column before imputation:")
print(df.isnull().sum())

# Replace missing values in numeric columns with the mean of each column
df[df.select_dtypes(include='number').columns] = df.select_dtypes(include='number').fillna(df.select_dtypes(include='number').mean())

# Verify that there are no missing values left
print("\nMissing values in each column after imputation:")
print(df.isnull().sum())

print("*" * 50)

#4.Filter the dataset to include only rows where the sepal length is greater than 5.0

df_filtered = df[df['Sepal.Length'] > 5.0]
print("Original dataset shape:", df.shape)
print("Filtered dataset shape:", df_filtered.shape)

#Filter the dataset to include only rows of the species 'Setosa'
df_setosa = df[df['Species'] == 'setosa']
print("Original dataset shape:", df.shape)
print("Filtered dataset shape:", df_setosa.shape)

print("*" * 50)

# 5.1.Calculate the mean, median, and standard deviation of petal length for each species
petal_length_stats = df.groupby('Species')[['Petal.Length']].agg(['mean', 'median', 'std'])
print(petal_length_stats)

#5.2 Count the number of occurrences of each species.
print(df['Species'].value_counts())

#5.3.Calculate the minimum and maximum petal width for each species.
print(df.groupby('Species')['Petal.Width'].agg(['min', 'max']))

#5.4.Find the species with the highest average sepal width.
print(df.groupby('Species')['Sepal.Width'].mean().sort_values(ascending=False).head(5))

print("*" * 50)

#6.1 Normalize the numerical features
numerical_features = ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width']
for feature in numerical_features:
    df[feature] = (df[feature] - df[feature].min()) / (df[feature].max() - df[feature].min())
print(df.head())
#6.2 Create a new column that is the ratio of petal length to petal width
df['petal_ratio'] = df['Petal.Length'] / df['Petal.Width']
print(df.head())

print("*" * 50)

# 7.1 Calculate the 25th, 50th, and 75th percentiles of sepal length for each species
percentiles = df.groupby('Species')['Sepal.Length'].quantile([0.25, 0.5, 0.75])
print(percentiles)

#7.2 Calculate the range (max - min) of petal length for each species
petal_length_range = df.groupby('Species')['Petal.Length'].agg(['min', 'max']).apply(lambda x: x['max'] - x['min'], axis=1)
print(petal_length_range)

print("*" * 50)

#8.1

species_info = {
    'setosa': {'habitat': 'Mediterranean regions', 'color': 'Red', 'size': 'Small'},
    'versicolor': {'habitat': 'Alpine meadows', 'color': 'White', 'size': 'Medium'},
    'virginica': {'habitat': 'Coastal regions', 'color': 'Orange', 'size': 'Large'}
}

species_df = pd.DataFrame(species_info).T.reset_index().rename(columns={'index': 'species'})

print(species_df)

#8.2 Create a new DataFrame with additional information about each species
species_info = {
    'Species': ['setosa', 'versicolor', 'virginica'],
    'typical_habitat': ['moist meadows', 'woodlands', 'coastal areas'],
    'average_height': [30, 60, 70],
    'flower_color': ['white', 'purple', 'pink']
}


df_species_info = pd.DataFrame(species_info)
# Merge the two DataFrames
df_merged = pd.merge(df, df_species_info, on='Species')
print(df_merged.head())

print("*" * 50)

#9.1 Define a custom function to categorize flowers based on petal length
def categorize_flowers(petal_length):
    if petal_length < 3:
        return 'small'
    elif petal_length < 5:
        return 'medium'
    else:
        return 'large'
 # Apply the custom function to the petal length column
df['flower_size'] = df['Petal.Length'].apply(categorize_flowers)
print(df.head())














