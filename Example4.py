# Example 4

import streamlit as st
import plotly.express as px
import pandas as pd

# Load Sample Data
df = px.data.gapminder()

# Streamlit App Title
st.title("📊 Interactive Dashboard with Multiple Plots")

# Create a sidebar filter for selecting a year
selected_year = st.sidebar.slider("Select Year:", int(df["year"].min()), int(df["year"].max()), int(df["year"].min()))

# Filter data based on the selected year
filtered_df = df[df.year == selected_year]

# Create three different plots
fig1 = px.scatter(filtered_df, x="gdpPercap", y="lifeExp", size="pop", color="continent",
                  hover_name="country", log_x=True, size_max=60, title="Life Expectancy vs GDP")

fig2 = px.bar(filtered_df, x="continent", y="pop", color="continent", title="Population per Continent")

fig3 = px.line(filtered_df, x="country", y="gdpPercap", color="continent", title="GDP Per Capita by Country")

# Layout - Using Tabs to Display Multiple Plots
tab1, tab2, tab3 = st.tabs(["📌 Scatter Plot", "📊 Bar Chart", "📈 Line Chart"])

with tab1:
    st.plotly_chart(fig1, use_container_width=True)

with tab2:
    st.plotly_chart(fig2, use_container_width=True)

with tab3:
    st.plotly_chart(fig3, use_container_width=True)

