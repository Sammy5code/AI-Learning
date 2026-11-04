import pandas as pd

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, root_mean_squared_error, r2_score
from sklearn.linear_model import Ridge
# IMPORTING THE DATA
data = fetch_california_housing(as_frame=True)
df = data.frame
X = df.drop("MedHouseVal", axis=1)
y = df["MedHouseVal"]

# PREPROCESSING
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# TRAINING THE MODEL
model = LinearRegression()
model.fit(X_train, y_train)

# PREDICTION
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

# EVALUATION
linear_mae = mean_absolute_error(y_test, y_test_pred)
linear_rmse = root_mean_squared_error(y_test, y_test_pred)
linear_r2 = r2_score(y_test, y_test_pred)

print("Linear Regression Results")
print("MAE:", linear_mae)
print("RMSE:", linear_rmse)
print("R²:", linear_r2)

# RIDGE REGRESSION
scaler = StandardScaler()
X_train_scale = scaler.fit_transform(X_train)
X_test_scale = scaler.transform(X_test)

model_ridge = Ridge()
model_ridge.fit(X_train_scale, y_train)

y_ridge_pred = model_ridge.predict(X_test_scale)

ridge_mae = mean_absolute_error(y_test, y_ridge_pred)
ridge_rmse = root_mean_squared_error(y_test, y_ridge_pred)
ridge_r2 = r2_score(y_test, y_ridge_pred)

print("Ridge Regression Results")
print("MAE:", ridge_mae)
print("RMSE:", ridge_rmse)
print("R²:", ridge_r2)


