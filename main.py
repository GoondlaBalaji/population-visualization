import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (skip metadata rows)
df = pd.read_csv(
    "population_dataset.csv",
    skiprows=4
)

# Select year
year = "2022"

# Remove rows with missing population
df_year = df[['Country Name', year]].dropna()

# Select top 10 countries by population
top10 = df_year.sort_values(by=year, ascending=False).head(10)

# Create bar chart
plt.figure()
plt.bar(top10['Country Name'], top10[year])

# Labels and title
plt.xlabel("Country")
plt.ylabel("Population")
plt.title(f"Top 10 Most Populous Countries ({year})")
plt.xticks(rotation=45)

# Show plot
plt.show()
