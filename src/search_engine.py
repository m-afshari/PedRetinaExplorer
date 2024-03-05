# src/search_engine.py
import pandas as pd
from src.utils import preprocess_data

def search_most_similar_patients(feature1, feature2):
    # Load the patient data and chemotherapy database
    patient_data = pd.read_csv("data/patient_data.csv")
    chemotherapy_data = pd.read_csv("data/chemotherapy_database.csv")

    # Preprocess data if needed
    # patient_data = preprocess_data(patient_data)
    # chemotherapy_data = preprocess_data(chemotherapy_data)

    # Implement your search logic here
    # Example: Finding patients with features close to the user input
    result = patient_data[(patient_data['Feature1'] - feature1).abs() < 0.1 &
                          (patient_data['Feature2'] - feature2).abs() < 0.1]

    # Return the top 5 most similar patients
    return result.head()