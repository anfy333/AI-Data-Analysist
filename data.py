import plotly.express as px
import pandas as pd

data = {
    'Year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
    'Aboveground_Biomass': [37.75, 58.20, 56.98, 61.91, 59.16, 62.76, 64.56, 66.78, 72.06, 68.58, 71.67, 69.12],  # Values in Mg per hectare
    'Belowground_Biomass': [18.95, 24.13, 24.49, 25.46, 25.53, 26.37, 27.45, 27.28, 28.02, 27.63, 28.26, 27.92]  # Values in Mg per hectare
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Create a line plot
fig = px.line(df, x='Year', y=['Aboveground_Biomass', 'Belowground_Biomass'],
              title='Trends in Aboveground and Belowground Biomass Over Time',
              labels={'value': 'Biomass (Mg per hectare)', 'variable': 'Biomass Type', 'Year': 'Year'},
              markers=True)

# Adding customization
fig.update_layout(
    xaxis_title="Year",
    yaxis_title="Biomass (Mg per hectare)",
    legend_title="Biomass Type"
)

# Show the plot
fig.show()