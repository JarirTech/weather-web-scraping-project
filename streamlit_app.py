import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px


st.title(" World Weather Temperatures Dashboard")
st.write(
    """
    This dashboard explores current weather temperatures across global cities.
    The data was scraped from timeanddate.com, cleaned using Pandas,
    stored in a SQLite database, and visualized using Streamlit and Plotly.
    """
)


conn = sqlite3.connect("./database/weather_data.db")
df = pd.read_sql("SELECT * FROM weather_data", conn)
conn.close()
#Data Visualization

#Vis 1: Line chart

# Aggregating and sorting


df_country_avg = (
    df.groupby("Country", as_index=False)["Temperature in F"]
      .mean()
      .sort_values("Temperature in F")
)
st.subheader("Average Temperature by Country")
fig1 = px.line(
    df_country_avg,
    x="Country",
    y="Temperature in F",
    markers=True,
    title="Average Temperature by Country (Sorted)"
)

fig1.update_layout(
    xaxis_tickangle=-45,
    xaxis_title="Country",
    yaxis_title="Average Temperature (°F)"
)

st.plotly_chart(fig1, use_container_width=True)

st.write(
    """
    **Insight:**  
    This chart shows the overall temperature trend across countries.
    Sorting by average temperature makes it easy to identify colder and warmer regions globally.
    """
)



# Vis 2: Temperatures by Country

st.subheader("City Temperatures by Country")

selected_country = st.selectbox(
    "Select a country:",
    sorted(df["Country"].unique())
)

df_selected = df[df["Country"] == selected_country]

fig2 = px.bar(
    df_selected,
    x="City",
    y="Temperature in F",
    title=f"Temperatures in {selected_country} Cities"
)

fig2.update_layout(
    xaxis_tickangle=-45,
    xaxis_title="City",
    yaxis_title="Temperature (°F)"
)

st.plotly_chart(fig2, use_container_width=True)

st.markdown("""
**Insight:**  
This chart reveals noticeable temperature variation between cities within the same country.
Larger countries tend to show wider temperature ranges due to differences in geography and climate zones.
""")


# Vis 3: Histogram chart
#Average temperature by country

st.subheader("Distribution of Temperatures")

fig3 = px.histogram(
    df,
    x="Temperature in F",
    nbins=15,
    title="Distribution of Temperatures Across All Cities"
)

fig3.update_layout(
    xaxis_title="Temperature (°F)",
    yaxis_title="Number of Cities"
)

st.plotly_chart(fig3, use_container_width=True)
st.write(
    """
    **Insight:**  
    The histogram shows that most cities fall within a moderate temperature range,
    while fewer cities experience extreme cold or heat.
    """
)

# conclusion:

st.subheader("Key Conclusions")

st.markdown(
    """
    1. Average temperatures vary significantly by country, reflecting geographic and climatic differences.
    2. U.S. cities show wide temperature variation depending on location and season.
    3. Most global cities experience moderate temperatures, with extremes being less common.

    **Limitations:**  
    - Data represents a single snapshot in time.
    - Weather conditions may change rapidly.
    - Some regions may be underrepresented.
    """
)