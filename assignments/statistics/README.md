# 📘 Assignment: Statistics with Python

## 🎯 Objective

Master statistical analysis and data manipulation using pandas and numpy. Learn to load, clean, explore, and analyze datasets while computing descriptive statistics, probability distributions, and hypothesis testing.

## 📝 Tasks

### 🛠️ Data Loading and Exploration with Pandas

#### Description
Load datasets into pandas DataFrames, explore their structure, and perform initial data quality checks and basic statistical summaries.

#### Requirements
Completed program should:

- Load data from CSV, Excel, and other file formats using pandas
- Inspect DataFrame structure: shape, columns, data types, dtypes
- Display first/last rows and basic information about the dataset
- Check for missing values and handle them (drop, fill, interpolate)
- Generate descriptive statistics: mean, median, std, quartiles, min, max
- Create summary reports of data quality and completeness
- Group data by columns and compute group statistics
- Identify and handle duplicate rows
- Filter and subset data based on conditions
- Example usage:
  ```python
  df = load_and_explore("data.csv")
  summary_stats = describe_dataset(df)
  ```

### 🛠️ Numerical Operations with NumPy

#### Description
Perform mathematical and statistical operations on arrays using NumPy for efficient numerical computing.

#### Requirements
Completed program should:

- Create and manipulate numpy arrays with different shapes and dimensions
- Perform element-wise and matrix operations
- Calculate statistical measures: mean, median, variance, standard deviation
- Compute percentiles and quantiles
- Generate random numbers from different distributions
- Perform linear algebra operations: matrix multiplication, transpose, inverse
- Apply numpy functions to arrays: sum, product, cumulative operations
- Use broadcasting for array operations
- Handle multidimensional arrays and reshaping
- Example usage:
  ```python
  arr = np.array([1, 2, 3, 4, 5])
  variance = np.var(arr)
  percentile_90 = np.percentile(arr, 90)
  ```

### 🛠️ Statistical Analysis and Hypothesis Testing

#### Description
Perform statistical analyses including correlation analysis, distribution testing, and hypothesis tests to draw meaningful conclusions from data.

#### Requirements
Completed program should:

- Calculate correlation coefficients (Pearson, Spearman)
- Create correlation matrices and identify relationships
- Perform normality tests on data distributions
- Conduct t-tests (one-sample, two-sample, paired)
- Perform ANOVA (Analysis of Variance) tests
- Calculate p-values and confidence intervals
- Implement chi-square tests for categorical data
- Perform regression analysis and calculate R-squared
- Visualize distributions and test results
- Document statistical findings and interpretation
- Example usage:
  ```python
  t_stat, p_value = scipy.stats.ttest_ind(group1, group2)
  correlation = df.corr()
  ```

### 🛠️ Data Cleaning and Transformation

#### Description
Clean raw data and transform it into a suitable format for analysis, handling missing values, outliers, and data inconsistencies.

#### Requirements
Completed program should:

- Identify and handle missing values (NaN, None)
- Detect and treat outliers (z-score, IQR methods)
- Standardize and normalize numerical features
- Encode categorical variables (one-hot encoding, label encoding)
- Create new features from existing data (feature engineering)
- Handle duplicates and inconsistent data types
- Perform data validation and quality checks
- Create data transformation pipelines
- Generate clean datasets ready for analysis
- Create comprehensive data cleaning reports
