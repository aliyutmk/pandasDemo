import pandas as pd
import numpy as np

# Create a date range from 2023-01-01 to 2023-12-31
date_range = pd.date_range(start='2023-01-01', end='2023-12-31')

# Generate random data for the other columns
sales = np.random.randint(1, 100, size=len(date_range))
departments = np.random.choice(['Dept1', 'Dept2', 'Dept3', 'Dept4'], size=len(date_range))
workers = np.random.randint(1, 50, size=len(date_range))

# Create the DataFrame
df = pd.DataFrame({
    'Year': date_range.year,
    'Month': date_range.month,
    'Sales': sales,
    'Department': departments,
    'Workers': workers
}, index=date_range)

print(df.head()) # Display the first few rows of the DataFrame
""" Convert dtype to datetime"""
df["Year"] = pd.to_datetime(df["Year"], format="%Y")
df["Month"] = pd.to_datetime(df["Month"])

"""groupby department and sum up the sales"""
workers_group = df.groupby('Department')['Sales'].sum()

"""Find the highest sales"""