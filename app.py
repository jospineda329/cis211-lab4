# CIS 211 Lab 4 starter
# Build a fictional campus club or service information page.
# Read CIS_211_Lab4_Guide.pdf before editing this file.
# This starter runs, but its TODO sections are not a completed submission.

import streamlit as st

# TODO 1: Replace these values with your own fictional club or service details.
# Keep at least three key-value pairs. You may add more.
club_info = {
    "name": "Your fictional club",
    "day": "Choose a fictional meeting day",
    "time": "Choose a fictional meeting time",
}

# TODO 2: Replace these sample strings with at least three relevant activities.
# During the list change check, add one new item and keep it in the final app.
activities = [
    "Replace with your first activity",
    "Replace with your second activity",
    "Replace with your third activity",
]

st.title(club_info["name"])
st.caption("A fictional CIS 211 course project. These are not real campus arrangements.")

# Remove this starter message when your page is complete.
st.write("Starter page: complete the TODO sections using the Lab 4 guide.")

st.header("About this club or service")
# TODO 3: Use st.markdown() to write your own two- or three-sentence introduction.
# Include both **bold** and *italic* text inside your Python string.
# The handout explains triple quotes if your Markdown spans several lines.

st.header("Activities or services")
# TODO 4: Write a for loop that displays every value from activities.
# Use Streamlit output inside the loop. Do not type each activity again.

st.header("Details")
# TODO 5: Display at least two dictionary values by looking them up by key.
# Give the displayed values meaningful labels such as Day and Time.

st.header("Prepare for a visit")
# TODO 6: Use st.markdown() to display a three-item Markdown list.
# Add one meaningful, working external Markdown link.

# TODO 7: Add at least three comments explaining your OWN completed code.
# TODO 8: Perform both change checks and complete the private submission template.
# Upload your final source files, links, reflection, and app screenshots to Brightspace.
