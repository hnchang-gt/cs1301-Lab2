# This creates the page for displaying data visualizations.

import streamlit as st
import json
from pathlib import Path
import pandas as pd
import altair as alt

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Visuals",
    page_icon="🍵",
)

# PAGE TITLE
st.title("Matcha and Tea Café Visualizations 🍵")


# PART 1: GRAPHS FROM data.json

json_path = Path(__file__).resolve().parent.parent / "data.json"

with open(json_path, "r") as file:
    data = json.load(file)

st.write(data["chart_title"])
st.subheader("My Favorite Café Locations")
st.map(data["data_points"])


st.subheader("Find a Café Within Your Budget")

st.slider(
    "Maximum drink price ($)",
    min_value=7.0,
    max_value=12.0,
    value=12.0,
    step=0.25,
    key="max_price"
)

filtered_cafes = []

for cafe in data["data_points"]:
    if cafe["price"] <= st.session_state["max_price"]:
        filtered_cafes.append(cafe)

if filtered_cafes:
    cafe_table = pd.DataFrame(filtered_cafes)
    st.metric(
        "Mean Drink Price",
        f"${cafe_table['price'].mean():.2f}"
    )

    st.metric(
        "Median Drink Price",
        f"${cafe_table['price'].median():.2f}"
    )

    chart = alt.Chart(cafe_table).mark_circle(size=120).encode(
        x=alt.X("price:Q", title="Price of My Usual Order ($)"),
        y=alt.Y(
            "taste_rating:Q",
            title="My Taste Rating",
            scale=alt.Scale(domain=[0, 10])
        ),
        tooltip=["label", "usual_order", "price", "taste_rating"]
    ).properties(
        title="Drink Price vs. Taste Rating"
    )

    st.altair_chart(chart, use_container_width=True)
else:
    st.write("No cafés fit this budget. Try increasing the maximum price.")

# PART 2: GRAPHS FROM data.csv
st.divider()
st.header("Café Survey Results")

csv_path = Path(__file__).resolve().parent.parent / "data.csv"

if csv_path.exists() and csv_path.stat().st_size > 0:
    survey_data = pd.read_csv(csv_path)

    if survey_data.empty:
        st.info("Complete the survey first to see the results.")
    else:
        st.dataframe(survey_data)
        st.subheader("Preferred Milk Types")

        milk_chart = alt.Chart(survey_data).mark_arc().encode(
            theta=alt.Theta("count():Q", title="Responses"),
            color=alt.Color("milk_preference:N", title="Milk Preference"),
            tooltip=[
                alt.Tooltip("milk_preference:N", title="Milk"),
                alt.Tooltip("count():Q", title="Responses")
            ]
        ).properties(
            title="Milk Preferences Among Survey Respondents"
        )

        st.altair_chart(milk_chart, use_container_width=True)

        st.subheader("Drink Budgets by Milk Preference")

        st.selectbox(
            "Choose a milk preference:",
            ["All", "Whole", "Oat", "Almond", "Soy",
             "Coconut", "No milk", "Other"],
            key="milk_filter"
        )

        if st.session_state["milk_filter"] == "All":
            filtered_responses = survey_data
        else:
            filtered_responses = survey_data[
                survey_data["milk_preference"]
                == st.session_state["milk_filter"]
            ]

        if filtered_responses.empty:
            st.info("No responses for this milk preference yet.")
        else:
            st.metric(
                "Mean Drink Budget",
                f"${filtered_responses['drink_budget'].mean():.2f}"
            )

            st.metric(
                "Median Drink Budget",
                f"${filtered_responses['drink_budget'].median():.2f}"
            )
            
            budget_chart = alt.Chart(filtered_responses).mark_bar().encode(
                x=alt.X(
                    "drink_budget:Q",
                    bin=alt.Bin(step=1),
                    title="Budget for One Drink ($)"
                ),
                y=alt.Y(
                    "count():Q",
                    title="Number of Respondents",
                    axis=alt.Axis(tickMinStep=1)
                ),
                tooltip=[
                    alt.Tooltip("count():Q", title="Respondents")
                ]
            ).properties(
                title="Distribution of Drink Budgets"
            )

            st.altair_chart(budget_chart, use_container_width=True)
            
        
else:
    st.info("No survey data has been saved yet.")
