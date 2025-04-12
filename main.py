# import  matplotlib.pyplot as pyplot

# labels = ("Python", "Javascript","Typescript", "NextJS", "React", "NodeJS", "HTML ", "CSS", "Tailwind CSS")
# sizes = (75, 75, 75, 80, 50, 70, 100, 75, 85)

# pyplot.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
# pyplot.show()



import streamlit as st
import matplotlib.pyplot as pyplot

# Set page config (optional)
st.set_page_config(page_title="My Skills Pie Chart", layout="centered")

# Title
st.title("🧠 My Tech Skills Distribution")

# Labels and sizes
labels = ("Python", "Javascript", "Typescript", "NextJS", "React", "NodeJS", "HTML", "CSS", "Tailwind CSS")
sizes = (75, 75, 75, 80, 50, 70, 100, 75, 85)

# Plotting
fig, ax = pyplot.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display in Streamlit
st.pyplot(fig)

st.markdown("---")
st.text("Created by Hadiqa Gohar | Powered by Placelogo")

