import streamlit as st
import os

def set_page_config():
    st.set_page_config(
        page_title="PedRetinaExplorer",
        page_icon=":hospital:",  # Change the icon as needed
        layout="centered",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': 'https://www.extremelycoolapp.com/help',
            'Report a bug': "https://www.extremelycoolapp.com/bug",
            'About': "# This is a header. This is an *extremely* cool app!"
        }
    )

def display_logo():
    # Get the absolute path to the image file
    current_directory = os.path.dirname(os.path.realpath(__file__))
    parent_directory = os.path.dirname(current_directory)
    image_path = os.path.join(parent_directory, "images", "logo.png")

    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.write("")

    with col2:
        st.image(image_path, width=300)

    with col3:
        st.write("")