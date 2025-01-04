import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read the first two lines to get column names and units
with open('buoys_data.csv', 'r') as file:
    columns = file.readline().strip().split(',')
    units = file.readline().strip().split(',')

# Combine column names with units
combined_columns = [f"{col} ({unit})" for col, unit in zip(columns, units)]


# Read the remaining data into a DataFrame
buoys = pd.read_csv('buoys_data.csv', skiprows=2, names=combined_columns)

# Ensure the 'time (UTC)' column is in datetime format if it exists
if 'time (UTC)' in buoys.columns:
    buoys['time (UTC)'] = pd.to_datetime(buoys['time (UTC)'])

# Set 'time (UTC)' as the index for resampling
buoys.set_index('time (UTC)', inplace=True)

print(buoys.head())
print(buoys.info())
print(buoys.iloc[:,4:8].describe())

# Define the years you want to include
years_to_include = [2023, 2024]

# Filter the DataFrame to include only the specified years
buoys_filtered = buoys[buoys.index.year.isin(years_to_include)]

# Resample the data to monthly means
buoys_monthly = buoys_filtered[['WaveHeight (meters)', 'WindSpeed (knots)', 'AirTemperature (degrees_C)', 'Gust (knots)']].resample('M').max()

# print(buoys_monthly.head())
# print(buoys_monthly.info())
# print(buoys_monthly.describe())   

# Plot the three line plots on a single chart with separate y-axes
fig, ax1 = plt.subplots(figsize=(20, 7))

# Plot WaveHeight on primary y-axis
sns.lineplot(data=buoys_monthly, x=buoys_monthly.index, y='WaveHeight (meters)', ax=ax1, color='tab:blue', label='WaveHeight (meters)')
ax1.set_ylabel('WaveHeight (meters)', color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')

# Create a secondary y-axis for WindSpeed
ax2 = ax1.twinx()
sns.lineplot(data=buoys_monthly, x=buoys_monthly.index, y='WindSpeed (knots)', ax=ax2, color='tab:orange', label='WindSpeed (knots)')
ax2.set_ylabel('WindSpeed (knots)', color='tab:orange')
ax2.tick_params(axis='y', labelcolor='tab:orange')

# Create a third y-axis for AirTemperature
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))  # Offset the third axis
sns.lineplot(data=buoys_monthly, x=buoys_monthly.index, y='AirTemperature (degrees_C)', ax=ax3, color='tab:green', label='AirTemperature (degrees_C)')
ax3.set_ylabel('AirTemperature (degrees_C)', color='tab:green')
ax3.tick_params(axis='y', labelcolor='tab:green')

# Create a fourth y-axis for Gust
ax4 = ax1.twinx()
ax4.spines['right'].set_position(('outward', 120))  # Offset the fourth axis
sns.lineplot(data=buoys_monthly, x=buoys_monthly.index, y='Gust (knots)', ax=ax4, color='tab:red', label='Gust (knots)')
ax4.set_ylabel('Gust (knots)', color='tab:red')
ax4.tick_params(axis='y', labelcolor='tab:red')

# Add legends
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
lines_3, labels_3 = ax3.get_legend_handles_labels()
lines_4, labels_4 = ax4.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2 + lines_3 + lines_4, labels_1 + labels_2 + labels_3 + labels_4, loc='upper left')

plt.title('WaveHeight, WindSpeed, AirTemperature, and Gust Over Time')
fig.tight_layout()
plt.show()

# Create the correlation matrix
columns_of_interest = ['WaveHeight (meters)', 'WindSpeed (knots)', 'AirTemperature (degrees_C)', 'Gust (knots)']
correlation_matrix = buoys[columns_of_interest].corr()
# Display the correlation matrix
print(correlation_matrix)

# Plot the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix')
plt.show()