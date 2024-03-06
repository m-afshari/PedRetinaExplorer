import streamlit as st
import pandas as pd
from scipy.spatial.distance import euclidean
import os
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
import time

from app_config import set_page_config, display_logo
from data_loader import load_sample_data

data, categorical_cols = load_sample_data()

# Function to calculate Euclidean distance
def calculate_distance(row, input_values):
    encoded_row = []
    for i, value in enumerate(row):
        if i < len(row) - len(categorical_cols):
            # For numerical features, find the nearest value in the data
            encoded_row.append(data.iloc[:, i].sub(value).abs().idxmin())
        else:
            # For categorical features, use the encoded value directly
            col_name = categorical_cols[i - (len(row) - len(categorical_cols))]
            encoded_row.append(value)

    distances = []
    for _, case in data.iterrows():
        distance = 0 #euclidean(encoded_row, list(case))
        distances.append(distance)
    return distances

def display_case_details(case_number, row):
    st.subheader(f"Case {case_number}")
    for feature, value in row.items():
        if feature != "distance":
            st.write(f"{feature}: {value}")

# Streamlit app
set_page_config()

# Horizontal menu
selected_tab = option_menu(None, ["Search Engine", "Upload Entry", "About"], 
    icons=['house', 'cloud-upload', "list-task"], 
    menu_icon="cast", default_index=0, orientation="horizontal")

if selected_tab == "Search Engine":
    # Left sidebar for input features
    with st.sidebar:

        st.title("Input Features")

        # Required input features
        date_toggle = st.toggle("Age in months")
        age = st.number_input("Diagnosis age in " + ("month" if date_toggle else "day"), step=1, key="age")
        gender = st.selectbox("Gender", ["Male", "Female"], key="gender")
        laterality = st.selectbox("Laterality", ["One-sided", "Both-sided"], key="laterality")
        studied_eye = st.selectbox("Studied eye", ["Left", "Right"], key="studied_eye")
        tumor_number = st.selectbox("Tumour number", ["Unifocal", "Multifocal"], key="tumour_number")
        if tumor_number == "Multifocal":
            num_tumor = st.number_input("Number of tumour", step=1, key="num_tumour")

        # Optional input features
        add_iirc_stage = st.toggle("IIRC stage in diagnosis")
        if add_iirc_stage:
            iirc_stage = st.select_slider(
                'Select the stage',
                options=['A', 'B', 'C', 'D', 'E'])
        else:
            iirc_stage = None

        add_quadrant = st.toggle("Add quadrant")
        if add_quadrant:
            quadrant = st.selectbox("Select quadrant ", ["Nasal", "Masters"], key="quadrant")
        else:
            quadrant = None

        add_extra = st.toggle("Add extra information")
        if add_extra:
            extra = st.text_area("Additional information:","")
        else:
            extra = None

        # Search button
        search = st.button("Search")

    # Main area for search results
    if search:
        with st.spinner('Searching the database...'):
            time.sleep(1)
        input_values = [age, gender]  # Required input features

        # Add optional input features if provided
        # if income is not None:
        #     input_values.append(income)
        # if education is not None:
        #     input_values.append(education)

        # Calculate distances
        distances = calculate_distance(input_values, data)
        data["distance"] = distances

        # Sort by distance
        data = data.sort_values(by="distance")

        # Display statistics for the 10 most similar cases
        st.header("Statistics for the 10 Most Similar Cases")
        st.write(data.head(10).describe())

        # Display details of the 3 most similar cases
        st.header("Details of the 3 Most Similar Cases")
        col_1, col_2, col_3 = st.columns([1, 1, 1])

        for i, (index, row) in enumerate(data.head(3).iterrows(), start=1):
            if i == 1:
                with col_1:
                    display_case_details(i, row)
            elif i == 2:
                with col_2:
                    display_case_details(i, row)
            elif i == 3:
                with col_3:
                    display_case_details(i, row)
        st.write("---")

elif selected_tab == "About":
    st.title("About")
    text = """
    PedRetinaExplorer emerges as a pivotal resource in pediatric ophthalmology, offering a sophisticated and user-friendly solution for exploring, assessing, and gaining insights into chemotherapy outcomes in children with retinal conditions. By combining advanced technology with medical expertise, this project aims to significantly contribute to the improvement of treatment strategies and overall care for young patients.

    **Disclaimer: This system is provided for research practice only and takes no responsibility for usage in practical medical settings. It should not be used as a substitute for professional medical advice, diagnosis, or treatment.**
    """
    st.markdown(text)

display_logo()