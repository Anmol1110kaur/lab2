"""
Python Statistics and Data Analysis Starter Code

This is a starter template for data analysis using pandas and numpy.
Implement the functions below to practice statistical analysis skills.

Implement the functions below to practice data analysis and statistics skills.

Key concepts to implement:
- Loading and exploring data with pandas
- Numerical operations with numpy
- Statistical analysis and hypothesis testing
- Data cleaning and transformation
- Drawing insights from data
"""

import pandas as pd
import numpy as np
from typing import List, Dict, Tuple, Optional, Union
import statistics
from scipy import stats


# ============================================================================
# TASK 1: Data Loading and Exploration with Pandas
# ============================================================================

def load_dataset(file_path: str) -> pd.DataFrame:
    """
    Load a dataset from CSV or Excel file
    
    Args:
        file_path: Path to the data file (CSV or Excel)
    
    Returns:
        pandas DataFrame containing the dataset
    
    Example:
        df = load_dataset("data.csv")
    """
    # TODO: Use pandas to load the file based on extension
    # TODO: Handle different file formats (CSV, Excel, etc.)
    # TODO: Return the DataFrame
    pass


def explore_dataset(df: pd.DataFrame) -> Dict[str, any]:
    """
    Generate a comprehensive exploration report of the dataset
    
    Returns:
        Dictionary with exploration results:
        {
            'shape': (rows, cols),
            'columns': list of column names,
            'dtypes': data types,
            'missing_values': count of missing values,
            'duplicates': count of duplicate rows,
            'memory_usage': memory in MB
        }
    
    Example:
        report = explore_dataset(df)
        print(f"Dataset shape: {report['shape']}")
    """
    # TODO: Get shape and columns
    # TODO: Check data types and missing values
    # TODO: Identify duplicates
    # TODO: Calculate memory usage
    # TODO: Return comprehensive report
    pass


def describe_numeric_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate descriptive statistics for numeric columns
    
    Returns:
        DataFrame with statistics: count, mean, std, min, 25%, 50%, 75%, max
    """
    # TODO: Use pandas describe() method
    # TODO: Include all relevant statistics
    # TODO: Return statistics DataFrame
    pass


def handle_missing_values(df: pd.DataFrame, strategy: str = "drop") -> pd.DataFrame:
    """
    Handle missing values in the dataset
    
    Args:
        df: Input DataFrame
        strategy: 'drop', 'fill_mean', 'fill_median', 'fill_zero', or 'forward_fill'
    
    Returns:
        DataFrame with missing values handled
    
    Example:
        df_clean = handle_missing_values(df, strategy="fill_mean")
    """
    # TODO: Check for missing values
    # TODO: Apply specified strategy to handle them
    # TODO: Return cleaned DataFrame
    pass


def identify_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Identify and return duplicate rows in the dataset
    
    Returns:
        DataFrame containing only duplicate rows
    """
    # TODO: Find duplicate rows
    # TODO: Return duplicates or their count
    pass


def group_and_aggregate(df: pd.DataFrame, group_col: str, 
                       agg_dict: Dict[str, str]) -> pd.DataFrame:
    """
    Group data by a column and perform aggregations
    
    Args:
        df: Input DataFrame
        group_col: Column name to group by
        agg_dict: Dictionary mapping column names to aggregation functions
                 {'column': 'mean', 'amount': 'sum', etc.}
    
    Returns:
        Aggregated DataFrame
    
    Example:
        agg_dict = {'amount': 'sum', 'price': 'mean'}
        result = group_and_aggregate(df, 'category', agg_dict)
    """
    # TODO: Group by specified column
    # TODO: Apply aggregation functions
    # TODO: Return aggregated result
    pass


def filter_dataset(df: pd.DataFrame, conditions: Dict[str, Tuple]) -> pd.DataFrame:
    """
    Filter dataset based on multiple conditions
    
    Args:
        df: Input DataFrame
        conditions: Dictionary mapping column names to (operator, value) tuples
                   {'age': ('>', 25), 'name': ('==', 'John')}
    
    Returns:
        Filtered DataFrame
    """
    # TODO: Apply multiple filter conditions
    # TODO: Handle different operators: ==, !=, >, <, >=, <=, 'in', 'not in'
    # TODO: Return filtered DataFrame
    pass


# ============================================================================
# TASK 2: Numerical Operations with NumPy
# ============================================================================

def create_numpy_arrays(data_list: List) -> np.ndarray:
    """Create a numpy array from a Python list"""
    # TODO: Convert list to numpy array
    pass


def array_statistics(arr: np.ndarray) -> Dict[str, float]:
    """
    Calculate statistical measures for a numpy array
    
    Returns:
        {
            'mean': float,
            'median': float,
            'std': float,
            'variance': float,
            'min': float,
            'max': float,
            'sum': float
        }
    """
    # TODO: Calculate mean, median, std, variance
    # TODO: Find min and max
    # TODO: Calculate sum
    # TODO: Return dictionary of statistics
    pass


def calculate_percentiles(arr: np.ndarray, percentiles: List[int]) -> Dict[int, float]:
    """
    Calculate specified percentiles of an array
    
    Example:
        calculate_percentiles(arr, [25, 50, 75])
        # Returns {25: 5.2, 50: 10.5, 75: 15.8}
    """
    # TODO: Use np.percentile for each percentile
    # TODO: Return dictionary mapping percentile to value
    pass


def normalize_array(arr: np.ndarray) -> np.ndarray:
    """
    Normalize array to have mean=0 and std=1 (z-score normalization)
    
    Example:
        normalized = normalize_array(arr)
    """
    # TODO: Calculate mean and std
    # TODO: Apply normalization formula: (x - mean) / std
    # TODO: Return normalized array
    pass


def scale_array(arr: np.ndarray, min_val: float = 0, max_val: float = 1) -> np.ndarray:
    """
    Scale array to specified range (min-max scaling)
    
    Example:
        scaled = scale_array(arr, 0, 1)
    """
    # TODO: Find min and max of array
    # TODO: Apply scaling formula: (x - min) / (max - min) * (max_val - min_val) + min_val
    # TODO: Return scaled array
    pass


def matrix_operations(matrix1: np.ndarray, matrix2: np.ndarray) -> Dict[str, np.ndarray]:
    """
    Perform various matrix operations
    
    Returns:
        {
            'sum': matrix sum,
            'product': matrix multiplication,
            'transpose_m1': transpose of matrix1,
            'determinant_m1': determinant,
            'inverse_m1': inverse (if square)
        }
    """
    # TODO: Add matrices
    # TODO: Multiply matrices (dot product)
    # TODO: Transpose matrix1
    # TODO: Calculate determinant (if square)
    # TODO: Calculate inverse (if square and non-singular)
    # TODO: Return dictionary of results
    pass


def generate_random_data(distribution: str, size: int, 
                        params: Dict = None) -> np.ndarray:
    """
    Generate random data from specified distribution
    
    Args:
        distribution: 'normal', 'uniform', 'exponential', 'poisson', etc.
        size: Number of samples
        params: Distribution parameters as dictionary
    
    Example:
        # Normal distribution with mean=0, std=1
        data = generate_random_data('normal', 1000, {'mean': 0, 'std': 1})
        
        # Uniform distribution between 0 and 10
        data = generate_random_data('uniform', 1000, {'low': 0, 'high': 10})
    """
    # TODO: Generate random samples from specified distribution
    # TODO: Handle different distribution types
    # TODO: Use provided parameters
    # TODO: Return random data array
    pass


# ============================================================================
# TASK 3: Statistical Analysis and Hypothesis Testing
# ============================================================================

def calculate_correlation(df: pd.DataFrame, method: str = "pearson") -> pd.DataFrame:
    """
    Calculate correlation matrix for numeric columns
    
    Args:
        df: Input DataFrame
        method: 'pearson', 'spearman', or 'kendall'
    
    Returns:
        Correlation matrix as DataFrame
    
    Example:
        corr_matrix = calculate_correlation(df, method="pearson")
    """
    # TODO: Use pandas corr() method with specified method
    # TODO: Return correlation matrix
    pass


def test_normality(data: Union[List, np.ndarray], test: str = "shapiro") -> Dict:
    """
    Test if data follows a normal distribution
    
    Args:
        data: Input data
        test: 'shapiro', 'normaltest', or 'anderson'
    
    Returns:
        {
            'statistic': test statistic,
            'p_value': p-value,
            'is_normal': bool (True if p-value > 0.05),
            'test_name': name of test used
        }
    
    Example:
        result = test_normality(data)
    """
    # TODO: Perform specified normality test using scipy.stats
    # TODO: Calculate p-value
    # TODO: Determine if data is normal (threshold 0.05)
    # TODO: Return results dictionary
    pass


def ttest_independent(group1: List, group2: List) -> Dict:
    """
    Perform independent samples t-test
    
    Returns:
        {
            't_statistic': float,
            'p_value': float,
            'mean_group1': float,
            'mean_group2': float,
            'significant': bool (True if p-value < 0.05)
        }
    
    Example:
        result = ttest_independent([1, 2, 3], [4, 5, 6])
    """
    # TODO: Use scipy.stats.ttest_ind
    # TODO: Calculate t-statistic and p-value
    # TODO: Calculate group means
    # TODO: Determine if significant (p < 0.05)
    # TODO: Return results dictionary
    pass


def ttest_paired(before: List, after: List) -> Dict:
    """
    Perform paired samples t-test
    
    Example:
        result = ttest_paired([before_scores], [after_scores])
    """
    # TODO: Use scipy.stats.ttest_rel
    # TODO: Calculate t-statistic and p-value
    # TODO: Return results dictionary
    pass


def chi_square_test(observed: List[int], expected: List[int]) -> Dict:
    """
    Perform chi-square goodness-of-fit test
    
    Returns:
        {
            'chi_square_statistic': float,
            'p_value': float,
            'significant': bool
        }
    """
    # TODO: Use scipy.stats.chisquare
    # TODO: Calculate chi-square statistic and p-value
    # TODO: Return results dictionary
    pass


def anova_test(*groups) -> Dict:
    """
    Perform one-way ANOVA test across multiple groups
    
    Example:
        result = anova_test([1, 2, 3], [4, 5, 6], [7, 8, 9])
    """
    # TODO: Use scipy.stats.f_oneway
    # TODO: Calculate F-statistic and p-value
    # TODO: Return results dictionary
    pass


def linear_regression(x: np.ndarray, y: np.ndarray) -> Dict:
    """
    Perform simple linear regression
    
    Returns:
        {
            'slope': float,
            'intercept': float,
            'r_squared': float,
            'correlation': float,
            'p_value': float
        }
    """
    # TODO: Calculate slope and intercept
    # TODO: Calculate R-squared and correlation
    # TODO: Calculate p-value
    # TODO: Return regression results
    pass


def confidence_interval(data: List, confidence: float = 0.95) -> Tuple[float, float]:
    """
    Calculate confidence interval for mean
    
    Args:
        data: Input data
        confidence: Confidence level (default 0.95 for 95% CI)
    
    Returns:
        Tuple of (lower_bound, upper_bound)
    
    Example:
        ci = confidence_interval(data, 0.95)
    """
    # TODO: Calculate mean and standard error
    # TODO: Calculate t-value for confidence level
    # TODO: Calculate bounds
    # TODO: Return confidence interval
    pass


# ============================================================================
# TASK 4: Data Cleaning and Transformation
# ============================================================================

def detect_outliers(arr: np.ndarray, method: str = "iqr") -> np.ndarray:
    """
    Detect outliers in data using IQR or z-score method
    
    Args:
        arr: Input array
        method: 'iqr' or 'zscore'
    
    Returns:
        Boolean array indicating which elements are outliers
    
    Example:
        outliers = detect_outliers(arr, method="iqr")
    """
    # TODO: Implement IQR method: Q3 + 1.5*IQR or similar
    # TODO: Implement z-score method: |z| > 3
    # TODO: Return boolean array of outliers
    pass


def remove_outliers(df: pd.DataFrame, columns: List[str], 
                    method: str = "iqr", threshold: float = 1.5) -> pd.DataFrame:
    """
    Remove outliers from DataFrame
    
    Args:
        df: Input DataFrame
        columns: Columns to check for outliers
        method: 'iqr' or 'zscore'
        threshold: IQR multiplier (default 1.5) or z-score threshold
    
    Returns:
        DataFrame with outliers removed
    """
    # TODO: Identify outliers using specified method
    # TODO: Remove rows containing outliers
    # TODO: Return cleaned DataFrame
    pass


def encode_categorical(df: pd.DataFrame, columns: List[str], 
                      method: str = "onehot") -> pd.DataFrame:
    """
    Encode categorical variables
    
    Args:
        df: Input DataFrame
        columns: Categorical columns to encode
        method: 'onehot' or 'label'
    
    Returns:
        DataFrame with encoded columns
    
    Example:
        df_encoded = encode_categorical(df, ['color', 'size'], method='onehot')
    """
    # TODO: Use pd.get_dummies for one-hot encoding
    # TODO: Use pd.factorize or LabelEncoder for label encoding
    # TODO: Return encoded DataFrame
    pass


def standardize_columns(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """
    Standardize numeric columns (z-score normalization)
    
    Example:
        df_standard = standardize_columns(df, ['age', 'income'])
    """
    # TODO: Calculate mean and std for each column
    # TODO: Apply standardization: (x - mean) / std
    # TODO: Return DataFrame with standardized columns
    pass


def normalize_columns(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """
    Normalize numeric columns to [0, 1] range
    
    Example:
        df_normalized = normalize_columns(df, ['age', 'income'])
    """
    # TODO: Calculate min and max for each column
    # TODO: Apply normalization: (x - min) / (max - min)
    # TODO: Return DataFrame with normalized columns
    pass


def create_features(df: pd.DataFrame, feature_specs: Dict[str, str]) -> pd.DataFrame:
    """
    Create new features from existing data
    
    Args:
        df: Input DataFrame
        feature_specs: Dictionary mapping new feature names to transformations
                      {'age_group': 'pd.cut(df.age, bins=[0, 18, 65, 100])', ...}
    
    Returns:
        DataFrame with new features added
    
    Example:
        specs = {'age_group': 'pd.cut(df.age, bins=[0, 18, 65, 100])'}
        df_new = create_features(df, specs)
    """
    # TODO: Create new features based on specifications
    # TODO: Support common transformations: binning, log, sqrt, ratios, etc.
    # TODO: Return DataFrame with new features
    pass


def clean_data_pipeline(df: pd.DataFrame, config: Dict) -> pd.DataFrame:
    """
    Execute a complete data cleaning pipeline
    
    Args:
        config: Configuration dictionary with cleaning steps
               {
                   'drop_columns': ['col1', 'col2'],
                   'handle_missing': 'drop',
                   'remove_duplicates': True,
                   'remove_outliers': True,
                   'standardize': ['age', 'income']
               }
    
    Returns:
        Cleaned DataFrame
    """
    # TODO: Drop unnecessary columns
    # TODO: Handle missing values
    # TODO: Remove duplicates
    # TODO: Remove outliers
    # TODO: Standardize/normalize columns
    # TODO: Return cleaned DataFrame
    pass


if __name__ == "__main__":
    # Example usage and testing
    print("Statistics and Data Analysis Assignment")
    print("========================================")
    
    # TODO: Add test code here to verify your implementations
    # Example:
    # df = load_dataset("data.csv")
    # report = explore_dataset(df)
    # print(f"Dataset shape: {report['shape']}")
