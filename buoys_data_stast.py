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

# Resample the data to monthly means, max, min, and std
buoys_monthly = buoys_filtered[['WaveHeight (meters)', 'WindSpeed (knots)', 'AirTemperature (degrees_C)', 'Gust (knots)']].resample('M').agg(['mean', 'max', 'min', 'std'])

print(buoys_monthly.head())
print(buoys_monthly.info())
print(buoys_monthly.describe())

# Plot WaveHeight
fig1, ax1 = plt.subplots(figsize=(14, 7))
sns.lineplot(data=buoys_monthly['WaveHeight (meters)'], x=buoys_monthly.index, y='mean', ax=ax1, color='tab:blue', label='WaveHeight (meters) Mean')
sns.lineplot(data=buoys_monthly['WaveHeight (meters)'], x=buoys_monthly.index, y='max', ax=ax1, color='tab:blue', linestyle='--', label='WaveHeight (meters) Max')
sns.lineplot(data=buoys_monthly['WaveHeight (meters)'], x=buoys_monthly.index, y='min', ax=ax1, color='tab:blue', linestyle=':', label='WaveHeight (meters) Min')
ax1.set_ylabel('WaveHeight (meters)', color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')
ax1.legend(loc='upper left')
ax1.set_title('WaveHeight Over Time')
fig1.tight_layout()
plt.show()

# Plot WindSpeed
fig2, ax2 = plt.subplots(figsize=(14, 7))
sns.lineplot(data=buoys_monthly['WindSpeed (knots)'], x=buoys_monthly.index, y='mean', ax=ax2, color='tab:orange', label='WindSpeed (knots) Mean')
sns.lineplot(data=buoys_monthly['WindSpeed (knots)'], x=buoys_monthly.index, y='max', ax=ax2, color='tab:orange', linestyle='--', label='WindSpeed (knots) Max')
sns.lineplot(data=buoys_monthly['WindSpeed (knots)'], x=buoys_monthly.index, y='min', ax=ax2, color='tab:orange', linestyle=':', label='WindSpeed (knots) Min')
ax2.set_ylabel('WindSpeed (knots)', color='tab:orange')
ax2.tick_params(axis='y', labelcolor='tab:orange')
ax2.legend(loc='upper left')
ax2.set_title('WindSpeed Over Time')
fig2.tight_layout()
plt.show()

# Plot AirTemperature
fig3, ax3 = plt.subplots(figsize=(14, 7))
sns.lineplot(data=buoys_monthly['AirTemperature (degrees_C)'], x=buoys_monthly.index, y='mean', ax=ax3, color='tab:green', label='AirTemperature (degrees_C) Mean')
sns.lineplot(data=buoys_monthly['AirTemperature (degrees_C)'], x=buoys_monthly.index, y='max', ax=ax3, color='tab:green', linestyle='--', label='AirTemperature (degrees_C) Max')
sns.lineplot(data=buoys_monthly['AirTemperature (degrees_C)'], x=buoys_monthly.index, y='min', ax=ax3, color='tab:green', linestyle=':', label='AirTemperature (degrees_C) Min')
ax3.set_ylabel('AirTemperature (degrees_C)', color='tab:green')
ax3.tick_params(axis='y', labelcolor='tab:green')
ax3.legend(loc='upper left')
ax3.set_title('AirTemperature Over Time')
fig3.tight_layout()
plt.show()

# Plot Gust
fig4, ax4 = plt.subplots(figsize=(14, 7))
sns.lineplot(data=buoys_monthly['Gust (knots)'], x=buoys_monthly.index, y='mean', ax=ax4, color='tab:red', label='Gust (knots) Mean')
sns.lineplot(data=buoys_monthly['Gust (knots)'], x=buoys_monthly.index, y='max', ax=ax4, color='tab:red', linestyle='--', label='Gust (knots) Max')
sns.lineplot(data=buoys_monthly['Gust (knots)'], x=buoys_monthly.index, y='min', ax=ax4, color='tab:red', linestyle=':', label='Gust (knots) Min')
ax4.set_ylabel('Gust (knots)', color='tab:red')
ax4.tick_params(axis='y', labelcolor='tab:red')
ax4.legend(loc='upper left')
ax4.set_title('Gust Over Time')
fig4.tight_layout()
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