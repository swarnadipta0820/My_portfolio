import streamlit as st
st.set_page_config(page_title="My Portfolio", layout="wide")
st.title("Hi, I'm Swarnadipta")
st.subheader("Data Analyst | Labour Studies & Social Protection")
st.write("Welcome to my portfolio")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Insights", "About Me"])

if page=="Projects":
    st.header("📊 My Projects")
    st.subheader ("Project 1: PHYSICAL ACTIVITY, DIETARY PRACTICES & HEALTH: A Study of I.T. Professionals in Bengaluru")
    st.write("""An individual’s diet and level of physical activity/inactivity are two of the most important determinants of a person’s health. Contemporary studies have seemed to state that there is significant level of association between a person’s involvement in physical activity at work and their health. It is also noteworthy that diet of individuals has changed in the recent times, with macro events like Globalization.
    Therefore, this research report attempts to explore the newly adopted dietary practices and occupational physical activity/inactivity of individuals engaged in I.T. sector of firms located in Bengaluru. The results have clearly shown that there has been a significant decrease in the levels of physical activity of the respondents. A surge can also be seen in the levels of sedentary time of the respondents. The dietary practices of the respondents have a somewhat balanced share of fruits, vegetables, cereals, fast-foods and other items in their major meals of the day, i.e., breakfast, lunch and dinner. However, the share of Fast-foods is more than 50% in case of snacks.
    Respondents also stated that they have experienced deteriorated levels of physical fitness in
the period post-employment. This can be linked to the reduction in levels of physical activity
while being at work. Respondents have also complained of various health conditions during
and after working hours.
    Despite the attempt made to accurately conduct the research, there were few limitations and
obstacles that were faced that are later discussed. The research report, finally, concludes with
the recommendations by professional researchers to reduce the vulnerabilities to Non-
Communicable Diseases.""")
    st.subheader("🎯Objectives")
    st.markdown("""
    - To explore the dietary practices of I.T. professionals residing in Bengaluru, Karnataka
    - To explore the occupational and leisurely physical activity of the I.T. professionals residing in Bengaluru, Karnataka
    """)
    st.subheader("🔍 Key Findings")
    st.markdown("""
    - Reduced physical activity coupled with leisure activities such as "sedentary activities" and "sleeping" could be contributing reasons for "Deteriorated Physical Fitness" (most common response with 76% occurrence)
    - Despite the prevelance of home-cooked food across meals, share of fast-food continues to capture a significant portion of the respondents' snacks between meals.
    - According to Petrillo and Meyers' (2002) findings, reliance on "fast-foods" could be a contributing factory to deteriorated physical fitness.
    - Involvement in predominantly sedentary jobs can lead to early onset of various non-communicable diseases (NCDs). Respondents have reported various conditions (inconsistent or erratic sleep patterns)  which could be pre-events to NCDs (Nobrega, et al., 2016).
    - Tokunaga et al. (2012) recommends the adoption of a mediterranean diet, rich in fruits, vegetables, canola oil, nuts and olive oil. Such a diet has provent to reduce the risk of developing NCDs, along with moderate levels of physical activity.
    - Hamilton et al (2008) suggests that people should stand more and sit less, along with brisk walking.
    """)

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Swarnadipta_BASS_DissertationResponses.csv")
st.dataframe(df)
gender_counts = df["What gender do you identify as?"].value_counts()
fig,ax = plt.subplots()
ax.pie(
    gender_counts,
    labels = gender_counts.index,
    autopct= "%1.1f%%",
    colors = ["#4C72B0","#DD8452","#55A868"],
    startangle=90
)
ax.set_title("Gender Distribution of Respondents")
st.pyplot(fig)

st.bar_chart(df["What is your income per annum?"].value_counts())



fitness_affect = df["How has your work affected your physical fitness/performance?"].value_counts()
fig1,ax1 = plt.subplots()
ax1.pie(
    fitness_affect,
    labels = fitness_affect.index,
    autopct= "%1.1f%%",
    colors = ["#4C72B0","#DD8452","#55A868"],
    startangle=90
)
ax.set_title("Self-reported Effects of work on Physical Fitness")
st.pyplot(fig1)

# snack_components = df["What kind of snacks do you have between meals (breakfast and lunch/lunch and dinner)? "].value_counts()
# fig2,ax2 = plt.subplots(figsize = (8,6))
# wedges, texts, autotexts = ax2.pie(
#     snack_components,
#     labels = None,
#     autopct="%1.1f%%",
#     colors =['b','g','r','m','y','c'],
#     startangle=90
# )

# ax2.legend(
#     wedges,
#     snack_components.index,
#     title = "Snack Types",
#     loc="center left",
#     bbox_to_anchor=(1,0,0.5,1),
#     fontsize=8
# )

# ax2.set_title("Components of Snacks")
# plt.tight_layout()
# st.pyplot(fig2)