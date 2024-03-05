# src/data_processing.py
import pandas as pd

def load_data(file_path):
    """
    Load the dataset from the specified file path.

    Parameters:
        file_path (str): Path to the dataset file.

    Returns:
        pd.DataFrame: Loaded dataset.
    """
    return pd.read_csv(file_path)

def preprocess_data(data):
    """
    Preprocess the dataset.

    Parameters:
        data (pd.DataFrame): Raw dataset.

    Returns:
        pd.DataFrame: Preprocessed dataset.
    """
    # Add your data preprocessing steps here
    # For example, handling missing values, encoding categorical variables, etc.

    # Example: Drop rows with missing values
    data = data.dropna()

    # Example: Convert categorical variables to numerical using one-hot encoding
    # data = pd.get_dummies(data, columns=['categorical_column'])

    return data