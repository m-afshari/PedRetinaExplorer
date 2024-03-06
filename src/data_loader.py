import pandas as pd

def load_sample_data():
    # Sample data
    data = pd.DataFrame({
        'age': [25, 35, 45, 55, 65, 28, 38, 48, 58, 68, 30, 40, 50, 60, 70, 32, 42, 52, 62, 72],
        'gender': ['M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F'],
        'income': [50000, 60000, 70000, 80000, 90000, 55000, 65000, 75000, 85000, 95000, 52000, 62000, 72000, 82000, 92000, 58000, 68000, 78000, 88000, 98000],
        'education': ['Bachelors', 'Masters', 'PhD', 'Bachelors', 'Masters', 'PhD', 'Bachelors', 'Masters', 'PhD', 'Bachelors', 'Masters', 'PhD', 'Bachelors', 'Masters', 'PhD', 'Bachelors', 'Masters', 'PhD', 'Bachelors', 'Masters']
    })

    # Encode categorical variables
    categorical_cols = ['gender', 'education']
    for col in categorical_cols:
        data[col], _ = pd.factorize(data[col])

    return data, categorical_cols