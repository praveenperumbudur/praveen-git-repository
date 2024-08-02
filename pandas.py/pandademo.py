import pandas as pd
import numpy as np

df = pd.read_csv("income.csv")
#print(df)_csv("income. csv") #reading the csv using pandas
income_dc = df. columns #all data columns from the income dataset
#print(income_dc)
#first 2 columns from the income dataset
#print(income_dc[:2])
#find datatypes for all the columns
#print(df.dtypes)
df.Y2008 = df.Y2008.astype(float) #converts integer type into float datatype
#print (df.dtypes)
#print ("total number of rows and columns:", df. shape)
#print ("total number of rows:", df. shape [0])
#print ("total number of columns:", df. shape [1])
print ("First Five Rows from income dataset")
#print (df.head())
print ("Last Five Rows from income dataset")
#print (df.tail())
print ("First three Rows from income dataset")
#print (df.head(3))
print ("Last three Rows from income dataset")
#print (df.tail (3))
print (df.iloc[0:5])

iris = pd.read_csv("iris.csv")
print(iris)