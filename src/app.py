# src/app.py
import streamlit as st
from src.search_engine import search_most_similar_patients

def main():
    st.title("Chemotherapy Search Engine")

    # User input for patient features
    feature1 = st.slider("Feature 1", 0.0, 1.0, 0.5)
    feature2 = st.slider("Feature 2", 0.0, 1.0, 0.5)
    # Add more sliders or input fields for other features

    if st.button("Search"):
        # Call the search engine function
        result = search_most_similar_patients(feature1, feature2)
        st.write("Top 5 Most Similar Patients:")
        st.write(result)

if __name__ == "__main__":
    main()