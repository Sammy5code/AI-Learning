# California Housing Price Prediction

## Project Overview

This project uses machine learning to predict median house values in California using the California Housing dataset from Scikit-learn.

The main objective was to understand and implement a traditional machine learning workflow, from data exploration and preprocessing to model training, evaluation, residual analysis, and model comparison.

This is a beginner machine learning project focused on developing a strong understanding of fundamental machine learning concepts.

## Dataset

The project uses the **California Housing dataset**, available through Scikit-learn.

- **Number of records:** 20,640
- **Number of input features:** 8
- **Target variable:** `MedHouseVal`
- **Data source:** 1990 U.S. Census

Each row represents a California census block group, not an individual house.

### Features

| Feature | Description |
|---|---|
| `MedInc` | Median income in the block group |
| `HouseAge` | Median house age |
| `AveRooms` | Average number of rooms |
| `AveBedrms` | Average number of bedrooms |
| `Population` | Block group population |
| `AveOccup` | Average household occupancy |
| `Latitude` | Geographic latitude |
| `Longitude` | Geographic longitude |

The target, `MedHouseVal`, represents median house value in units of $100,000.

## Technologies and Libraries

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn

## Project Workflow

### 1. Data Loading

Loaded the California Housing dataset using Scikit-learn and converted it into a Pandas DataFrame for analysis.

### 2. Exploratory Data Analysis (EDA)

Explored the dataset to understand its structure, distributions, and relationships.

Activities included:

- Inspecting the dataset's shape and information.
- Checking for missing values.
- Examining descriptive statistics.
- Exploring feature distributions and potential outliers.
- Visualising relationships between features and the target.
- Examining correlations between numerical features.

### 3. Data Preprocessing

Separated the dataset into:

- **Features (`X`):** The eight input variables.
- **Target (`y`):** `MedHouseVal`.

Split the data into training and testing sets using an 80:20 ratio.

- **Training records:** 16,512
- **Testing records:** 4,128

### 4. Model Training

Trained a Linear Regression model using Scikit-learn.

The model learned relationships between the input features and median house values.

### 5. Model Evaluation

Evaluated the model using three regression metrics:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R-squared (R²)

### 6. Residual Analysis

Investigated the model's prediction errors to understand where and how its predictions differed from actual values.

Activities included:

- Calculating residuals.
- Plotting residuals against predictions.
- Examining the residual distribution.
- Identifying an observation with an unusually large prediction error.
- Comparing overpredictions and underpredictions.

### 7. Model Improvement Experiment

Experimented with Ridge Regression to investigate whether regularisation and feature scaling could improve model performance.

Used `StandardScaler` to scale the input features. The scaler was fitted on the training data and then applied to the test data to avoid data leakage.

## Model Performance

The following results were obtained on the test set:

| Metric | Linear Regression | Ridge Regression |
|---|---:|---:|
| MAE | 0.533200 | 0.533193 |
| RMSE | 0.745581 | 0.745557 |
| R² | 0.575788 | 0.575816 |

### Results Interpretation

Ridge Regression achieved slightly better scores across all three metrics. However, the differences were extremely small.

This experiment showed that regularisation did not produce a meaningful improvement over the original Linear Regression model on this dataset and split.

The baseline model explained approximately **57.58% of the variance** in the test-set target values.

Since the target is measured in units of $100,000:

- **Linear Regression MAE:** Approximately $53,320.
- **Linear Regression RMSE:** Approximately $74,558.

These results provide a useful baseline, but they also show that the model has room for improvement.

## Key Lessons Learned

Through this project, I gained practical experience with:

- Loading and exploring real-world datasets.
- Working with Pandas DataFrames.
- Understanding feature-target separation.
- Splitting data into training and testing sets.
- Training a Linear Regression model.
- Understanding model coefficients.
- Evaluating regression models using MAE, RMSE, and R².
- Understanding and analysing residuals.
- Identifying unusual observations.
- Applying feature scaling.
- Understanding the purpose of Ridge Regression.
- Comparing machine learning models using evaluation metrics.
- Avoiding data leakage during preprocessing.

## Conclusion

This project helped me understand how a traditional machine learning regression problem is approached from beginning to end.

Rather than focusing only on obtaining a high score, I focused on understanding the workflow, interpreting model results, investigating errors, and evaluating a possible improvement.

This is one step in my continued journey towards becoming an AI/ML engineer.

## Future Improvements

Possible future experiments include:

- Trying other regression algorithms.
- Investigating feature engineering techniques.
- Exploring the effects of outliers and unusual observations.
- Comparing different models using cross-validation.
- Improving model performance through carefully controlled experiments.

---

**Author:** Sammytech  
**Project:** California Housing Price Prediction  
**Language:** Python