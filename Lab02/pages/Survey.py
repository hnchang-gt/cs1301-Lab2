# This creates the page for users to input data.
# The collected data should be appended to the 'data.csv' file.

import streamlit as st
import pandas as pd
import csv
from pathlib import Path
csv_path = Path(__file__).resolve().parent.parent / "data.csv"
import os # The 'os' module is used for file system operations (e.g. checking if a file exists).

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Survey",
    page_icon="📝",
)

# PAGE TITLE AND USER DIRECTIONS
st.title("Your Café Favorites 🍵")
st.write("Tell me about your café preferences and drink budget!")

# DATA INPUT FORM
# 'st.form' creates a container that groups input widgets.
# The form is submitted only when the user clicks the 'st.form_submit_button'.
# This is useful for preventing the app from re-running every time a widget is changed.
with st.form("survey_form"):
    # Create text input widgets for the user to enter data.
    # The first argument is the label that appears above the input box.
    favorite_cafe = st.text_input("What'syour favorite café?")
    milk_preference = st.selectbox(
        "What milk do you prefer?",
        ["Whole", "Oat", "Almond", "Soy", "Coconut", "No milk", "Other"]
    )
    drink_budget = st.number_input(
        "What's your usual budget for one drink ($)?",
        min_value=0.0,
        value=8.0,
        step=0.25
    )
    drinks_per_week = st.number_input(
        "How many café drinks do you buy per week?",
        min_value=0,
        value=1,
        step=1
    )

    # The submit button for the form.
    submitted = st.form_submit_button("Submit Data")

    # This block of code runs ONLY when the submit button is clicked.
    if submitted:
        if favorite_cafe.strip() == "":
            st.warning("Please enter your favorite café.")
        else:
            with open(csv_path, "a", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow([
                    favorite_cafe.strip(),
                    milk_preference,
                    drink_budget,
                    drinks_per_week
                ])

            st.success("Your response has been saved!")
        
        st.write(f"Your favorite café is {favorite_cafe}, and your drink budget is ${drink_budget:.2f}.")


# DATA DISPLAY
# This section shows the current contents of the CSV file, which helps in debugging.
st.divider() # Adds a horizontal line for visual separation.
st.header("Current Data in CSV")

# Check if the CSV file exists and is not empty before trying to read it.
if csv_path.exists() and csv_path.stat().st_size > 0:
    # Read the CSV file into a pandas DataFrame.
        current_data_df = pd.read_csv(csv_path)
    # Display the DataFrame as a table.
        st.dataframe(current_data_df)
else:
    st.warning("The 'data.csv' file is empty or does not exist yet.")
