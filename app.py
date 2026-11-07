import streamlit as st

club_info = {
    "name": "Campus Creators Collective",
    "day": "Thursdays",
    "time": "6:00 PM",
}

activities = [
    "Video Film and Editing",
    "Audience Engagement",
    "Brainstorming and Planning",

]

st.title(club_info["name"])
st.caption("A fictional CIS 211 course project. These are not real campus arrangements.")

st.header("About this club or service")

st.markdown("""
**Campus Creators Collective** focuses on social media content creation and marketing.   
The objective is to help students build an online community and brand that represents them and their goals.
Here we will *develop ideas*, *plan and edit content* and share tips to *increase engagement*.
""")

st.header("Activities or services")

# this loop shows all the activities without needing to write them out because the for loop goes through each item on the list.
for activity in activities:
    st.write(activity)
st.header("Details")

# This shows how the dictionary has saved the values and uses the words day and time to retrieve that information.
st.write("Club Name:", club_info["name"])
st.write("Meeting Day:", club_info["day"])
st.write ("Meeting Time:", club_info["time"])

# This lists what is expected to bring to each club session, it keeps it organized in an easy to read format.
st.header("Prepare for a visit")
st.markdown("""
- Phone or Tablet of choice
- Notebook
- Ideas
""")
st.markdown("[Youtube Creators](https://www.youtube.com/creators/)")
