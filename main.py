import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Sample data
data = pd.DataFrame({
    'months': [6, 12, 24, 36],
    'cost': [1000, 2020, 3500, 5000]
})

X = data[['months']]
y = data['cost']

model = LinearRegression()
model.fit(X, y)

# Test prediction
print(model.predict([[18]]))