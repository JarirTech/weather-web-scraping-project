# weather-web-scraping-project



## Project Overview
This project is an interactive **Streamlit web application** that visualizes weather data stored in a SQLite database.  
The goal is to demonstrate strong data visualization practices, clear insights, and reproducibility using **Plotly Express** and **Streamlit**.

The application allows users to explore temperature patterns across countries and cities using multiple chart types and interactive controls.

---

## Dataset
- Source: SQLite database (`weather_data.db`)
- Key columns:
  - `Country`
  - `City`
  - `Date`
  - `Temperature in F`
  - `weather condition`



## Visualizations

### Visualization 1: Average Temperature by Country (Line Chart) static
- Displays average temperature per country.
- Sorted to make comparisons easier.
- Highlights differences in overall climate trends across countries.

**Insight:**  
Countries show noticeable variation in average temperatures, allowing quick identification of warmer and cooler regions.

---

### Visualization 2: City Temperatures by Selected Country (Bar Chart – Interactive)
- Users select a country from a dropdown.
- Displays city-level temperatures for the selected country.

**Insight:**  
Within a single country, city temperatures vary significantly, suggesting regional or geographic differences even at a national level.

---

### Visualization 3: Temperature Distribution (Histogram)static
- Shows the distribution of temperatures across all cities.
- Helps identify common temperature ranges and outliers.

**Insight:**  
Most city temperatures cluster within a specific range, with fewer extreme values, indicating moderate overall variability.

---

## Key Conclusions
1. Average temperatures differ clearly across countries, making country-level aggregation useful for high-level comparisons.
2. City-level data reveals meaningful variation within the same country.
3. Temperature values tend to cluster within a limited range, with few extreme outliers.

---

## Technologies Used
- Python
- Streamlit
- Plotly Express
- Pandas
- SQLite

---

##  Run the App Locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
