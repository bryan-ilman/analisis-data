import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.title("Bike Sharing Dashboard")
data = pd.read_csv("../data/day.csv")

st.sidebar.title("Information:")
st.sidebar.markdown("**Nama: Bryan Raihan 'Ilman**")

st.sidebar.title("Bike Sharing Dataset")
if st.sidebar.checkbox("Show Dataset"):
    st.subheader("Raw Data")
    st.write(data)
if st.sidebar.checkbox("Show Statistics"):
    st.subheader("Descriptive Statistics")
    st.write(data.describe())

st.sidebar.markdown('''
    - yr (0: 2011, 1: 2012)
    - season (1: Spring, 2: Summer, 3: Fall, 4: Winter)
    - weathersit (1: Clear, 2: Mist, 3: Snow, 4: Rain)
    - cnt: Total bike rentals
''')
st.sidebar.markdown("For more info, visit https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset?select=day.csv")

name_dict = {
    "season": {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"},
    "yr": {0: "2011", 1: "2012"},
    "weekday": {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}
}
data = data.replace(name_dict)

st.subheader("Bike Rentals Over Time")
year = st.selectbox("Select Year:", ["2011", "2012"])
filtered_data = data[data["yr"] == year]
fig = px.line(filtered_data, x="dteday", y="cnt", title=f"Bike Rentals in {year}", labels={"dteday": 'Year'})
st.plotly_chart(fig)

st.subheader("Casual and Registered Users")
weekday = st.selectbox("Select Weekday:", ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])
filtered_data = data[data["weekday"] == weekday]
fig = go.Figure(data=[go.Pie(labels=["Casual", "Registered"], values=[filtered_data["casual"].sum(), filtered_data["registered"].sum()])])
st.plotly_chart(fig)
