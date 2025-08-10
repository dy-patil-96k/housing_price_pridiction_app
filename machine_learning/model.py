# steps
# 1.load the data 
# 2.analyse the data 
# 3.clean the data 
# 4.visualize the data
# 5.train the model
# 6.evaluate the model
# 7.save the model
# 8.create a flask app to predict the price


# 0.import libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score,accuracy_score

# 1.load the data
df = pd.read_csv('C:\\Users\\Server\\Desktop\\pro\\ml\\projects\\best_projects\\housing price pridiction\\housing_data.csv')
# print(df.head())

# 2.analyse the data
# print(df.info())
# print(df.describe())
# Only select numeric columns for correlation
# corr_matrix = df.corr(numeric_only=True)
# print(corr_matrix['price'].sort_values(ascending=False))
# we have mostly relation 'sqft_living ,sqft_above ,bathrooms ,view,sqft_basement,bedrooms'

# 3.clean the data
df = df[['price','sqft_living','sqft_above','bathrooms','view','sqft_basement','bedrooms']]
# print(df.head())

# 4.data visualization

# 5.train test split
x = df[['sqft_living','sqft_above','bathrooms','view','sqft_basement','bedrooms']]
y = df[['price']]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
# Check the training data
print(x_test.tail())


# 6.train the model
model= LinearRegression()
model.fit(x_train, y_train)

# 7.evaluate the model
y_pred = model.predict(x_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print (f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')

import joblib
# Save the model
joblib.dump(model, 'housing_price_model.pkl')

