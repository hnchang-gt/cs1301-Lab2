# This creates the main landing page for the Streamlit application.
# Contains an introduction to the project and guide users to other pages.

# Import Streamlit
import streamlit as st

# st.set_page_config() is used to configure the page's appearance in the browser tab.
# It's good practice to set this as the first Streamlit command in your script.
st.set_page_config(
    page_title="Heien's Café Guide",  # The title that appears in the browser tab
    page_icon="🍵",         # An emoji that appears as the icon in the browser tab
)

# WELCOME PAGE TITLE
st.title("Heien's Matcha & Tea Guide 🍵")

# INTRODUCTORY TEXT
st.write("""
Welcome to my Matcha & Tea Guide! 🍵 As someone who loves trying new
drinks and exploring cafés, I created this guide to share seven of
my favorite spots around the Atlanta area.

You’ll find my usual orders, their prices, and my personal taste
ratings out of 10. Prices reflect my usual order at each café,
rather than the same drink everywhere.

Find café locations on the map and adjust the budget slider to
compare drinks within your spending limit. You can also explore
survey results showing milk preferences and drink budgets.
The mean and median values update with your selected filters.

Visit the Survey page to tell me your favorite café, preferred milk,
usual drink budget, and how many café drinks you buy each week.
Your response will contribute to the survey charts!
""")

# OPTIONAL: ADD AN IMAGE
# 1. Navigate to the 'images' folder in your Lab02 directory.
# 2. Place your image file (e.g., 'welcome_image.png') inside that folder.
# 3. Uncomment the line below and change the filename to match yours.
#
# st.image("images/welcome_image.png")
