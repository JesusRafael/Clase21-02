import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load Data:
df = pd.read_csv("/content/university_student_dashboard_data.csv")

# 2. Sidebar Filters:
st.sidebar.header("Filters")
program = st.sidebar.multiselect("Select Term:", df["Term"].unique())
year = st.sidebar.selectbox("Select Year:", df["Year"].unique())

# 3. Filter Data:
filtered_df = df[(df["Term"].isin(program)) & (df["Year"] == year)]

# 4. Admissions Section:
st.header("Admissions")
col1, col2, col3 = st.columns(3)
with col1:
  st.subheader("Total Applications")
  st.metric(label="Applications", value=filtered_df["Applications"].sum())
with col2:
  st.subheader("Admitted Rate")
  admitted_rate = (filtered_df["Admitted"].sum() / filtered_df["Applications"].sum()) * 100
  st.metric(label="Rate", value=f"{admitted_rate:.2f}%")
with col3:
  st.subheader("Enrollment Rate")
  enrollment_rate = (filtered_df["Enrolled"].sum() / filtered_df["Applications"].sum()) * 100
  st.metric(label="Rate", value=f"{enrollment_rate:.2f}%")

# 5. Retention Section:
st.header("Retention")
st.subheader("Retention Rate by Year")

retention_by_year = df.groupby('Year')['Retention Rate (%)'].mean().reset_index()

fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(x='Year', y='Retention Rate (%)', data=retention_by_year, ax=ax)
ax.set_title('Retention Rate by Year')
ax.set_xlabel('Year')
ax.set_ylabel('Retention Rate (%)')
st.pyplot(fig)

# 6. Satisfaction Section:
st.header("Student Satisfaction")
average_satisfaction = df.groupby('Year')['Student Satisfaction (%)'].mean().reset_index()
fig = px.bar(average_satisfaction, x='Year', y='Student Satisfaction (%)', 
             title='Average Satisfaction by Year')
st.plotly_chart(fig)

# 7. 
st.header("Enrollment by Program")
program_names = df.columns[7:]
enrollment_data = []
for program in program_names:
  total_enrollment = df[program].sum()
  enrollment_data.append([program, total_enrollment])

enrollment_df = pd.DataFrame(enrollment_data, columns=['Program', 'Enrolled'])

fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x='Program', y='Enrolled', data=enrollment_df, ax=ax)
ax.set_title('Enrollment by Program')
ax.set_xlabel('Program')
ax.set_ylabel('Number of Enrolled Students')
plt.xticks(rotation=45, ha='right')
st.pyplot(fig)

# 8. 
spring_df = df[df['Term'] == 'Spring']
fall_df = df[df['Term'] == 'Fall']

spring_applications = spring_df['Applications'].sum()
fall_applications = fall_df['Applications'].sum()
spring_enrolled = spring_df['Enrolled'].sum()
fall_enrolled = fall_df['Enrolled'].sum()

terms = ['Spring', 'Fall']
applications = [spring_applications, fall_applications]
enrolled = [spring_enrolled, fall_enrolled] 

x = np.arange(len(terms))  
width = 0.35 

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, applications, width, label='Applications')
rects2 = ax.bar(x + width/2, enrolled, width, label='Enrolled')

ax.set_ylabel('Number')
ax.set_title('Comparison of Spring vs. Fall Terms')
ax.set_xticks(x)
ax.set_xticklabels(terms)
ax.legend()

st.pyplot(fig)
